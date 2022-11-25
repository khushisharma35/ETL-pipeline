import sys
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject/')
from extraction .api_connection import data,fooditem
from load .insertdata import insert_food
from load .insertdata import insert_nutrients


food_details =[]
nutrients =[]
food_details.append(fooditem)
if data['currentPage'] is not None:
    for item in data['foods'][0]:
        id = data['foods'][0]['fdcId']
        description = data['foods'][0]['description']
        category = data['foods'][0]['foodCategory']

    food_details.extend([id, description, category])
    insert_food(fooditem, id, description, category)
    print(food_details)

    required_nutrientsid = [1003, 1004, 1008, 1253, 1257, 1087, 1089]
    nutrientsidname={1003:'Protein',1004:'Total lipid(fat)',1008:'Energy',1253:'cholesterol',1257:'Fatty acids,total trains',1087:'Calcium,ca',1089:'Iron,Fe'}
    for item in data['foods'][0]['foodNutrients']:
        if item['nutrientId'] in required_nutrientsid:
            id=item['nutrientId']
            name= item['nutrientName']
            value=item['value']

            nutrients.append([id,name])
            insert_nutrients(id,name)

    print(nutrients)

