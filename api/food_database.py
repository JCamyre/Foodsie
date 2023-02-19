
# TODO: FIX THIS ONE
# STILL THE SAME AS USERS_DATABASE

# # Required imports
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
food_ref = db.collection('foods')  # get the Food

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
        food_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

# randomly choose 50 random food pictures for the user to choose at first 
@app.route('/init', methods=['GET'])
def init():
    """
    init(): returns a list of 50 random food pictures from the database 
    """
    to_choose = []
    f = open('./init_recs.json')
    for line in f:
        data = json.loads(line)
        to_choose.append(data['photo_id'])

    choices = list(random.choices(to_choose, k=50))
    return choices


@app.route('/list', methods=['GET'])
def read():
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

@app.route('/update', methods=['POST', 'PUT'])
def update():
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

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        food_id = request.args.get('id')
        food_ref.document(food_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)