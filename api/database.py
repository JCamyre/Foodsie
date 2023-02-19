# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS
import json
import random
from query_recs import get_model_info, extract_food, generate_item_rec, regenerate_item_rec


# Initialize Flask app
app = Flask(__name__)

# Add CORS so that React can access backend
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize Firestore DB
cred = credentials.Certificate('./key.json')
default_app = initialize_app(cred)
db = firestore.client()
food_ref = db.collection('foods')  # get the Food
users_ref = db.collection('users')  # get the Users


# Syntax ... url/add?id=this-id
# we want to get this-id


@app.route('/food-add', methods=['POST'])
def food_create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        food_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

# randomly choose 50 random food pictures for the user to choose at first


@app.route('/init', methods=['GET'])
def food_init():
    """
    init(): returns a list of 50 random food pictures from the database 
    """
    to_choose = []
    f = open('./cleaned_yelp_photos.json')
    for line in f:
        data = json.loads(line)
        to_choose.append(data['photo_id'])

    choices = list(random.choices(to_choose, k=50))
    return choices


@app.route('/food-list', methods=['GET'])
def food_read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        food : Return document that matches query ID.
        all_foods : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        food_id = request.args.get('id')
        if food_id:
            food = food_ref.document(food_id).get()
            return jsonify(food.to_dict()), 200
        else:
            all_foods = [doc.to_dict() for doc in food_ref.stream()]
            return jsonify(all_foods), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/food-update', methods=['POST', 'PUT'])
def food_update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        food_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/user-add', methods=['POST'])
def user_create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        users_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

# user is done inputting favorited restaurants


@app.route('/finished', methods=['GET', 'POST'])
def user_finished():
    """
    finished() : post the "liked" foods into the firebase
    input: pass in an array of food_ids
    url/finished?id=id&foods=
    """
    try:
        user_id = request.args.get('id')
        food_list = request.args.get('foods')
        cuisines = request.args.get('c')
        # food_list = ['test']
        if user_id:
            if cuisines:
                cuisines_list = [cuisines]
            else:
                cuisines_list = []

            food_list = food_list[1:len(food_list) - 1]
            food_list = food_list.split(',')
            food_list = [s[1:len(s) - 1] for s in food_list]
            print(food_list)

            field_updates = {"food": food_list,
                            "cuisines": cuisines_list}

            users_ref.document(user_id).update(field_updates)
            return jsonify({"success": True}), 200
        else:
            raise Exception("No user inputted")

    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/user-list', methods=['GET'])
def user_read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        user : Return document that matches query ID.
        all_users : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        user_id = request.args.get('id')
        if user_id:
            user = users_ref.document(user_id).get()
            return jsonify(user.to_dict()), 200
        # else:
        #     all_users = [doc.to_dict() for doc in users_ref.stream()]
        #     return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/user-update', methods=['POST', 'PUT'])
def user_update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        users_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route('/genrecs', methods=['GET', 'POST'])
def genrecs():
    """"
    genrecs(): generates the recommendations based on the user profile
    input: user_id
    We take user_id, and we grab the list of foods that they like
    Call the food_firebase, get corresponding captions and put in a list
    Feed into the query_recs function
    Return recommendation, which is a str
    """
    try:
        # Check if ID was passed to URL query
        user_id = request.args.get('id')
        if user_id:
            user = users_ref.document(user_id).get()
            foods = (user.to_dict())['food']

            food_captions = []
            for item in foods:
                cap = food_ref.document(item).get().to_dict()['caption']
                food_captions.append(cap)

            extracted = extract_food(food_captions)

            cuisines = users_ref.document(user_id).get().to_dict()['cuisines']

            if cuisines == []:
                cuisines = None

            rec = generate_item_rec(extracted, cuisines)['choices'][0]['text']
            users_ref.document(user_id).update({'rec': rec})

            return rec, 200
        else:
            all_users = [doc.to_dict() for doc in users_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


# TODO: FIX
@app.route('/regen', methods=['GET'])
def regen():
    """"
    regen(): generates new recommendations based on their dislikes likes
    input: id, disliked flavors (str), disliked foods (str), new cultures (str) 
    We take user_id, and we grab the original generation
    Return new recommendation, which is a str
    """
    try:
        # Check if ID was passed to URL query
        user_id = request.args.get('id')
        dis_flavors = request.args.get('dfl')
        dis_foods = request.args.get('dfo')
        new_cultures = request.args.get('nc')

        if user_id:
            user = users_ref.document(user_id).get()
            orig_rec = (user.to_dict())['rec']

            if dis_flavors:
                dis_flavors = [dis_flavors]
            else:
                dis_flavors = []
            
            if dis_foods:
                dis_foods = [dis_foods]
            else:
                dis_foods = []

            if new_cultures:
                new_cultures = [new_cultures]
            else:
                new_cultures = []
                
            rec = regenerate_item_rec(orig_rec, dis_flavors, dis_foods, new_cultures)['choices'][0]['text']
            users_ref.document(user_id).update({'rec': rec})

            return rec, 200
        else:
            all_users = [doc.to_dict() for doc in users_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
