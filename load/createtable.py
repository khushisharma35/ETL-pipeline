def create_food_item():
    sql= """create table food_item(id SERIAL primary key,
                                    fdcId int,
                                    Name varchar(50),
                                    Description varchar(100),
                                    Category varchar(100));"""
    return sql
def create_nutrients():
    sql= """create table nutrients(id SERIAL ,
                                    nutrientId int primary key,
                                    Name varchar(50));"""
    return sql

def create_food_nutrients_mapping():
    sql=""" create table food_nutrients_mapping(id SERIAL primary key,
                        foodId int,
                        nutrientId int,
                        values float,
                        foreign key(foodId) references food_item(id),
                        foreign key(nutrientId) references nutrients(nutrientId));"""
    return sql
def create_recipe():
    sql = """create table recipe(id SERIAL primary key,
                  foodName varchar(50),
                  Recipe varchar(100));"""
    return sql