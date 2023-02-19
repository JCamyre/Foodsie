# TODO: FIX THIS ONE
# STILL THE SAME AS USERS_DATABASE


# # Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("./key.json")
default_app = initialize_app(cred)
db = firestore.client()
food_ref = db.collection("foods")  # get the Foods
biz_ref = db.collection("businesses")  # get the businesses

# Syntax ... url/add?id=this-id
# we want to get this-id
@app.route("/add", methods=["POST"])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json["id"]
        food_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route("/list", methods=["GET"])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        user : Return document that matches query ID.
        all_users : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        user_id = request.args.get("id")
        if user_id:
            user = food_ref.document(user_id).get()
            return jsonify(user.to_dict()), 200
        else:
            all_users = [doc.to_dict() for doc in food_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route("/update", methods=["POST", "PUT"])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json["id"]
        food_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route("/delete", methods=["GET", "DELETE"])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        user_id = request.args.get("id")
        food_ref.document(user_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@app.route("/business_fetch", methods=["GET"])
def fetch_businesses():
    try:
        user_id = request.args.get("id")
        food_doc = food_ref.document(user_id).get()
        food_data = food_doc.to_dict()
        business_id = food_data["business_id"]
        business_data = biz_ref.document(business_id).get().to_dict()
        name, address, city, state, postal_code, stars, review_count = (
            business_data["name"],
            business_data["address"],
            business_data["city"],
            business_data["state"],
            business_data["postal_code"],
            business_data["stars"],
            business_data["review_count"],
        )
        res = {
            "name": name,
            "address": address,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "stars": stars,
            "review_count": review_count,
        }
        return jsonify(res), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


port = int(os.environ.get("PORT", 8080))
if __name__ == "__main__":
    app.run(threaded=True, host="127.0.0.1", port=port)
