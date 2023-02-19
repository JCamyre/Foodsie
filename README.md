# FUGMA

## Inspiration

We wanted to create a platform that could amplify people's ability to enjoy food— to find more foods that they enjoy, to find others with similar tastes in food to connect with, or to be involved in the cultural exchange that is enabled by food. We found additional inspiration in Pinterest; the platform's ability to enable users to "catalogue [their] ideas" and build up from image and idea amalgamations was the catalyst for our project. 

Foodsie aims to highlight the best qualities of food, bridging users (their current tastes, their favorite foods) to new foods, new cultures, and new people.

## What it does

In its current iteration, Foodsie enables the user to provide their cuisine preferences: what dishes they like and dislike, what cuisines they generally enjoy, etc. We then generate embeddings for these user preferences, utilizing NLP techniques to create internal representations for the user's tastes. Using a nearest neighbor algorithm, we identify foods, cuisines, and restaurants that  fit the user's preference's flavor profiles, offering adaptive suggestions that we hope will help broaden their enjoyed foods to new dishes and new cultures. 

## How we built it

Built the frontend with React. We built a full Python and Flask backend (data contained in Firebase), and we utilized a transformer for natural language generation.

## Challenges we ran into

We found the limited time-frame of our project to be a significant challenge. When we began, we each had an ambitious vision for where we were going to take Foodsie over the weekend. As we continued to work, we were forced to adjust those expectations in order to create a solid MVP— forcing us to scale back to prioritize the brainstorming for our model, to thoroughly debug code written by multiple team members in a product setting, and to focus on improving our familiarity with the tools we used (OpenAI APIs, React, Firebase). 

## Accomplishments that we're proud of

We're proud of how our organized our workflow was for a team that had just come together for the weekend. We wrote extensive documentation, we delegated tasks successfully, and we kept effective channels of communication open between our team members. The result ended up being something that each of us was happy with: a solid MVP that was a strong step forward in our vision for the project. 

## What we learned

- Building a new platform from scratch is both time-consuming and difficult to do in only a few hours; we consistently had to scale back our expectations.
- We learned a lot about integrating multiple frameworks and multiple team members' code in building an effective and impactful application. 
- On the more technical side, we gained more experience with utilizing OpenAI and Firebase's APIs and training word embedding models. 

## What's next for Foodsie

Our main priority moving forward is to incorporate the community aspect of 
the app, where users are not only able to generate recommendations for themselves
but also are able to see what others are eating and being suggested as well.
Beyond that, there is plenty to improve and iterate upon for Foodsie: continuing
to improve our model to generate even more personalized food suggestions for users,
offering information on alternative sources for enjoying dishes (cookbooks, different
authors and YouTubers, etc.), and expanding our database to include an even greater
range of food and cuisines in our model. 
