import openai as ai
import os
import typing
from typing import List, Tuple

"""
Set env variable OPENAI_API_KEY to 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.
"""

STANFORD_ORG_ID = "org-cB9pEd5E9DW746jSupwICGuh"

ai.organization = STANFORD_ORG_ID
ai.apikey = os.getenv("OPENAI_API_KEY")


# get info on model we're using
def get_model_info(model: str = "text-davinci-003") -> None:
    """
    Prints model info, including owner, id, parent, permissions
    :param model: id of model that you're querying
    :return: None
    """

    print(ai.Model.retrieve(model))

text = '''Given that I like Chicken Tikka Masala, Boba, Filet Mignon, Soba Noodles, and Chow Fun, recommend me a flavor
         profile, as well as some food recommendations.'''

print(ai.Completion.create(
  model="text-davinci-003",
  prompt='''Given that I like Chow Fun, Chow Mein, and Orange Chicken, create a description of my flavor profile, describing
  what kinds of flavors I like, as well as one new flavor to try. Then, generate some recommendations for other food I should try
  based on my preferences, as well as one additional new food suggestion outside of my cultural preferences.''',
  max_tokens=1000,
  temperature=0
))


def generate_item_rec(liked_foods: List[str], new_cultures: List[str]) -> str:

    pass

def regenerate_item_rec(orig_input: str, orig_completion: str, disliked_flavors: List[str], disliked_foods: List[str], new_cultures: List[str]) -> str:

    pass
