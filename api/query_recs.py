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


def extract_food(captions: List[str]) -> List[str]:

    """
    Takes in yelp captions and returns out the food items that the pictures are describing.
    :param captions: List of captions generated by users on the yelp dataset
    :return: List of the food items in the pictures.
    """

    prompt = f"""Take the input texts {captions} and extract only the names of the food items in the text. Do not include accessory words.
   Some examples of this task include the input "Chow Mein, fried, so good" which extracts "Chow Mein", and the input "Fried Chicken with Honey, a delicious meal." which
    extracts "Fried Chicken with Honey". Another example is the input "Fried softshell crab, fried shrimp, fried fish" which extracts "Fried softshell crab, fried shrimp, fried fish."
    Another example is the input "Grilled Porkchop for two" extracts "Grilled Porkchop". 
                """
    completion = ai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1000, temperature=0
    )
    food_items = completion["choices"][0]["text"].strip("\n")
    return food_items.split(",")


def generate_item_rec(liked_foods: List[str], new_cultures: any = None) -> str:

    """
    Generates food recommendation scheme given foods that the user liked on the app.
    User can optionally supply specific cultures they want to try.
    :param liked_foods: List of foods that the user liked on the app.
    :param new_cultures: List of cultures or regions that the user is interested in trying.
    :return: Output prompt from LM
    """

    prompt = f"""
              Given that I like {liked_foods}, create a description of my flavor profile, describing
   what kinds of flavors I like, as well as one new flavor to try. Then, generate some recommendations for other food I should try
   based on my preferences, as well as one additional new food suggestion outside of my cultural preferences.
              """
    if new_cultures is not None:
        prompt = f"""
              Given that I like {liked_foods}, describe my flavor profile, explaining
   what kinds of flavors I like, as well as one new flavor to try and why. Then, generate some recommendations for other food I should try
   based on my preferences, with a short explanation of what each dish is. Finally, generate some food recommendations 
   from the following cultures: {new_cultures}, with a short explanation of what each dish is.
              """

    res = ai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1000, temperature=0
    )
    return res


def regenerate_item_rec(
    orig_input: str,
    disliked_flavors: List[str],
    disliked_foods: List[str],
    new_cultures: List[str],
) -> str:
    """
    If a user is unsatisfied with the initial generation we can regenerate it for them, excluding disliked flavors
    and disliked foods. Optionally can provide new cultures for further suggestions in the second iteration.

    :param orig_input:
    :param disliked_flavors:
    :param disliked_foods:
    :param new_cultures:
    :return:
    """
    first_idx, end_idx = orig_input.find("like"), orig_input.find("create")
    orig_liked_foods = orig_input[first_idx : end_idx - 1]
    orig_liked_foods = orig_liked_foods.split(",")
    liked_foods = orig_liked_foods
    extra_dislikes_prompt, new_cultures_prompt, disliked_foods_prompt = (
        "",
        """Then, generate some recommendations for other food I should try
   based on my preferences, as well as one additional new food suggestion outside of my cultural preferences.""",
        ""
    )

    if len(disliked_foods) > 0:
        disliked_foods = set(disliked_foods)
        liked_foods = [food for food in orig_liked_foods if food not in disliked_foods]
        disliked_foods_prompt = f"Do not suggest the following foods in your suggestions: {disliked_foods}"
    if len(disliked_flavors) > 0:
        extra_dislikes_prompt = f" Additionally, for the new recommendations, do not include flavors that include {disliked_flavors}. "
    if len(new_cultures) > 0:
        new_cultures_prompt = f"""Then, generate some recommendations for other food I should try based on my preferences. Additionally, suggest me some food options from the {new_cultures} food cultures, with a short explanation of each dish."""
    prompt = f"""Given that I like {liked_foods}, create a description of my flavor profile, describing what kinds of flavors I like, as well as one new flavor to try.{disliked_foods_prompt}{extra_dislikes_prompt}{new_cultures_prompt}"""
    res = ai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1000, temperature=0
    )
    return res


def main():
    print(regenerate_item_rec(orig_input="""Given that I like Fried Chicken, Waffles, and Chicken Noodle Soup, create a description of my flavor profile, describing
       what kinds of flavors I like, as well as one new flavor to try. Then, generate some recommendations for other food I should try
       based on my preferences. Finally, generate some food recommendations from the following cultures: African, with a short explanation of what each dish is.""",
                              disliked_flavors=["Sweet"], disliked_foods=["macaroni and cheese"],
                              new_cultures=["African"]))


if __name__ == "__main__":
    main()
