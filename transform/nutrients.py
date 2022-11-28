from load .insertdata import insert_nutrients
from load .insertdata import insert_food_nutrients_mapping
nutrientsIdName={1003:'Protein',1004:'Total lipid(fat)',1008:'Energy',1253:'cholesterol',1257:'Fatty acids,total trains',1087:'Calcium,ca',1089:'Iron,Fe'}

def nutrient():
    for id, name in nutrientsIdName.items():
        NutrientId = id
        NutrientName = name


        try:
            insert_nutrients(NutrientId,NutrientName)
        except :
            pass

def nutrientvalue(data):
    foodnutrient=data["foods"][0]["foodNutrients"]
    for val in  range(0, len(foodnutrient)):

        inutrientId=foodnutrient[val]['nutrientId']
        if inutrientId in nutrientsIdName.keys() :
            value =foodnutrient[val]["value"]
            insert_food_nutrients_mapping(inutrientId,value)

