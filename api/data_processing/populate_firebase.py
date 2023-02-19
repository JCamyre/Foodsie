import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account.
cred = credentials.Certificate('api/key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

f = open('api/data_processing/cleaned_yelp_photos.json')

i = 1

for line in f:
    if i % 100 == 0:
        print(i, " of 55331")
    data = json.loads(line)
    new_data = {'photo_id': data['photo_id'],
                'business_id': data['business_id'], 
                'caption': data['caption']}

    db.collection('foods').document(data['photo_id']).set(new_data)

    i += 1

    