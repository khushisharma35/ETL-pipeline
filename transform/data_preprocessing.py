
from transform .nutrients import nutrientvalue
from transform .nutrients import nutrient
from load .insertdata import insert_food
def food_data(data,fooditem):
    if data['totalPages'] is not None:
        nutrientvalue(data)
        nutrient()
        fdcId =data["foods"][0]["fdcId"]
        description =data["foods"][0]["description"]
        category = data["foods"][0]["foodCategory"]
        insert_food(fdcId, fooditem, description, category)



