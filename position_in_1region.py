import json

# preps in which 1st object has greater z value than 2nd
deeper_preps = [' behind ', ' against ', ' inside ', ' back ']

# 1st has lower z value
shallower_preps = [' outside ', ' front ', ' in front of ']

with open('subset_data\\region_graphs.json') as region_graph:
    data = json.load(region_graph)
    # for image in data:
    image = data[2]
    print("id",image['image_id'])
    regions = image['regions']
    # print(len(regions))
    for region in regions:
        # if any(word in region['phrase'] for word in deeper_preps):
        print(region['phrase'])
        print(region['relationships'])
        # print(region['objects'])


with open('subset_data\\objects.json') as objects:
    data = json.load(objects)
    # print(type(data))
    # print(json.dumps(data[1]['objects'], indent=4, sort_keys=True))
    # print(data[1]['objects'])
