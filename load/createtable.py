# def create_food_item():
#     sql= """ create table food_item( name varchar(100),
#               id int primary key,
#               description varchar(100),
#               category varchar(100));"""
#     return sql
def create_nutrients():
    sql= """create table nutrients(id int primary key,
                                    nutrientname varchar(50));"""
    return sql

def create_foodnutrientsmapping():
    sql=""" create table food_nutrient_mapping(id SERIAL primary key,
                        foodId int,
                        nutrient_id int,
                        values float,
                        foreign key(foodId) references food_item(id),
                        foreign key(nutrient_id) references nutrients(id));"""
    return sql