import json

f = open('/Users/wesley/Development/TreeHacks 2023/yelp_photos.json')
dest = open('/Users/wesley/Development/TreeHacks 2023/FUGMA/api/data_processing/cleaned_yelp_photos.json', 'w')

for line in f:
    data = json.loads(line)

    if data['caption'] != '' and data['label'] == 'food':
        dest.write(line)
    

