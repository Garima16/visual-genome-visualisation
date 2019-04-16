from visual_genome import api
# ids = api.get_image_ids_in_range(start_index=2000, end_index=2010)
# print(ids[0])


# image = api.get_image_data(id=2001)
# print(image)

# regions = api.get_region_descriptions_of_image(id=2001)
# print(len(regions))

# graph = api.get_region_graph_of_region(2001, 5553058)
# print(graph)
# print(graph.objects)


# def getXY(id):
#     regions = api.get_region_descriptions_of_image(id)
#     print(len(regions))
#     for region in regions:
#         print("x position:", region.x, "y position:", region.y)
#         # pass
#
#
# def getZ(id):
#     pass


# getXY(2001)

import json

prepositions = ['on', 'above', 'below', 'close to', 'next to', 'over', 'across', 'by', 'down', ]

# list of prepositions
# y_prepositions = ['on', 'above', 'over', 'down', '']

# first object deeper than 2nd
deeper_preps = ['behind', 'against', 'inside', 'outside', '']

with open('data\\15region_graphs.json') as att_syn:
    data = json.load(att_syn)

    # get 1 image data

    # data has 2 keys : image_id, regions
    image1 = data[1]
    # print(type(image1))
    # print(image1.keys())

    # get keys in 'regions'

    regions = image1['regions']  # list
    print(regions[1].keys())

    # get those phrases for which relationship is not empty

    # for region in regions:
        # if len(region['relationships']):
            # print(region['phrase'])

    for region in regions:
            # print(region['phrase'])

    # print("printing objects")

    # for region in regions:
    #     objects = region['objects']
    #     for object in objects:
    #         print(object['name'])

    # get phrasees of all regions
    regions = image1['regions']
    # for region in regions:
    #     print(region['phrase'])

    # print(json.dumps(data[0], indent=4, sort_keys=True))
    # print(type(data))
    # print(type(regions))
    # print("keys:", )
    # print(data.keys())
    # print(len(data.keys()))
