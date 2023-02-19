import json
import random

f = open('api/data_processing/cleaned_yelp_photos.json')
dest = open('api/init_recs.json', 'w')

count = 0
i = 0
r = random.randint(0, 500)

for line in f:
    if count == 200:
        break
    elif i == r:
        data = json.loads(line)
        dest.write(line)
        count += 1
        r = random.randint(0, 9)
        i = 0
    else:
        i += 1
    
