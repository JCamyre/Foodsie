# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import json
import random
from query_recs import get_model_info, extract_food, generate_item_rec, regenerate_item_rec

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('./key.json')
default_app = initialize_app(cred)
db = firestore.client()
users_ref = db.collection('users')  # get the Users
food_ref = db.collection('foods')  # get the Foods

# Syntax ... url/add?id=this-id
# we want to get this-id
@app.route('/add', methods=['POST'])
def create():
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
def finished():
    """
    finished() : post the "liked" foods into the firebase
    input: pass in an array of food_ids
    url/finished?id=id&foods=
    """
    try:
        user_id = request.args.get('id')
        food_list = request.args.get('foods')
        food_list = ['test']
        if user_id:
            field_updates = {"food": food_list}
            users_ref.document(user_id).update(field_updates)
            return jsonify({"success": True}), 200
        else:
            raise Exception("No user inputted")
            
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list', methods=['GET'])
def read():
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
        else:
            all_users = [doc.to_dict() for doc in users_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
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

# generate recommendations
@app.route('/genrecs', methods=['GET'])
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
            rec = generate_item_rec(extracted)
            return rec, 200
        else:
            all_users = [doc.to_dict() for doc in users_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)