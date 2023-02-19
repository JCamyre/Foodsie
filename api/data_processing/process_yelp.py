import json

f = open('api/data_processing/yelp_photos.json')
dest = open('api/data_processing/cleaned_yelp_photos.json', 'w')

for line in f:
    data = json.loads(line)

    if data['caption'] != '' and data['label'] == 'food':
        dest.write(line)
    

