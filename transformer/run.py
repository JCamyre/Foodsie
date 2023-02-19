import numpy as np
import torch
import torch.nn as nn
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
import argparse
import os


import dataset
import model
import trainer
import utils


argp = argparse.ArgumentParser()
argp.add_argument('function', help="Choose pretrain, finetune, or evaluate")
argp.add_argument('variant', help="Choose vanilla or perceiver") 
argp.add_argument('--bottleneck_dim', type=int, default=32)
argp.add_argument('pretrain_corpus_path', default=None)
argp.add_argument('--reading_params_path',default=None)
argp.add_argument('--writing_params_path',default=None)
argp.add_argument('--finetune_corpus_path', default=None)
argp.add_argument('--eval_corpus_path', default=None)
argp.add_argument('--outputs_path', default=None)
argp.add_argument('--pretrain_lr', default=6e-3, type=float)
argp.add_argument('--finetune_lr', default=6e-4, type=float)
argp.add_argument('--tb_expt_name', help='debug string for tb log.',
                  default='run')
args = argp.parse_args()

# Save the device
device = torch.cuda.current_device() if torch.cuda.is_available() else 'cpu'

# TensorBoard training log
writer = SummaryWriter(log_dir='expt/%s/%s_%s_%d_pt_lr_%f_ft_lr_%f' % (
    args.function,
    args.tb_expt_name,
    args.variant,
    args.bottleneck_dim,
    args.pretrain_lr,
    args.finetune_lr))

# Keep the block size 128
block_size = 128
text = open(args.pretrain_corpus_path, encoding='utf-8').read()
pretrain_dataset = dataset.CharCorruptionDataset(text, block_size)

# We don't suggest you change these hyperparameters, as they're known to work.
# use them for both the vanilla and the perceiver models
mconf = model.GPTConfig(pretrain_dataset.vocab_size, pretrain_dataset.block_size,
    n_layer=4, n_head=8, n_embd=256)

"""
Don't change above here; write your code below
"""

# define models.
# note: models should moved to device defined on line 34.

if args.variant == 'vanilla':
    model = model.GPT(mconf).to(device)  # just make a GPT model with the predefined hyperparams
elif args.variant == 'perceiver':
    # set mconf.perceiver, and mconf.bottleneck_dim parameters appropriately.
    mconf.perceiver = True
    mconf.bottleneck_dim = args.bottleneck_dim
    model = model.GPT(mconf).to(device)
else:
    raise ValueError("Unknown model variant")

# Perform pretraining, finetuning, or evaluation
if args.function == 'pretrain':
    assert args.writing_params_path is not None
    print("Begining pretrain...")
    tconf = trainer.TrainerConfig(max_epochs=650,
                          batch_size=128,
                          learning_rate=args.pretrain_lr,
                          lr_decay=True,
                          warmup_token=512 * 20,
                          final_tokens=200 * len(pretrain_dataset) * block_size,
                          num_workers=4,
                          writer=writer)
    trainer = trainer.Trainer(model, pretrain_dataset, None, tconf)   # set up trainer from module
    trainer.train()
    torch.save(model.state_dict(), args.writing_params_path)   # save to WRITING params path
    print("Pretraining finished...")

elif args.function == 'finetune':
    assert args.writing_params_path is not None
    assert args.finetune_corpus_path is not None

    DEFAULT_MAX_EPOCHS = 65   # adjust if needed
    if args.reading_params_path is not None:   # we have a pretrain to load
        model.load_state_dict(torch.load(args.reading_params_path))
        DEFAULT_MAX_EPOCHS = 10  # We pretrained so set the max epochs to lower

    tconf = trainer.TrainerConfig(max_epochs=DEFAULT_MAX_EPOCHS,
                          batch_size=256,
                          learning_rate=args.finetune_lr,
                          lr_decay=True,
                          warmup_tokens=512 * 20,
                          final_tokens=200 * len(pretrain_dataset) * block_size,
                          num_workers=2,
                          writer=writer)
    text = open(args.finetune_corpus_path, encoding='utf-8').read()    # get text for dataset
    train_dataset = dataset.NameDataset(pretrain_dataset, text)
    trainer = trainer.Trainer(model, train_dataset, None, tconf)
    trainer.train()
    # save to args.writing_params_path
    torch.save(model.state_dict(), args.writing_params_path)

elif args.function == 'evaluate':
    assert args.outputs_path is not None
    assert args.reading_params_path is not None
    assert args.eval_corpus_path is not None
    model.load_state_dict(torch.load(args.reading_params_path))
    correct = 0
    total = 0
    with open(args.outputs_path, 'w', encoding='utf-8') as fout:
        predictions = []
        for line in tqdm(open(args.eval_corpus_path, encoding='utf-8')):
            x = line.split('\t')[0]
            x = x + '⁇'
            x = torch.tensor([pretrain_dataset.stoi[s] for s in x], dtype=torch.long)[None,...].to(device)
            pred = utils.sample(model, x, 32, sample=False)[0]
            completion = ''.join([pretrain_dataset.itos[int(i)] for i in pred])
            pred = completion.split('⁇')[1]
            predictions.append(pred)
            fout.write(pred + '\n')
        total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    if total > 0:
        print(f'Correct: {correct} out of {total}: {correct/total*100}%')
    else:
        print(f'Predictions written to {args.outputs_path}; no targets provided')

