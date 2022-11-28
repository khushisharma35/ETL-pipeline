import sys
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject/')
from load import databaseconnection

from transform import nutrients

def insert_food(fdcId,Name,description,Category):
    sql= f"""insert into food_item(fdcId,Name,Description,Category) values({fdcId},'{Name}','{description}','{Category}')"""

    db_obj = databaseconnection.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)
    return sql
def insert_nutrients(nutrientId,nutrientName):
    sql = f"""insert into nutrients(nutrientId,Name) values({nutrientId},'{nutrientName}')"""
    db_obj = databaseconnection.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)
    return sql
def insert_food_nutrients_mapping(nutrientId,value):
    foodid=get_food_id()[0]
    sql=f""" insert into food_nutrients_mapping(foodId,nutrientId,values)values({foodid},{nutrientId},{value})"""
    db_obj = databaseconnection.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)
    return sql
def insert_recipe(fooditem,foodrecipe):

    sql= f"""insert into recipe(foodname,recipe)values('{fooditem}','{foodrecipe}')"""
    db_obj = databaseconnection.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)
    return sql


def get_food_id():
    sql = f"""SELECT MAX(id) FROM food_item;"""
    db_obj = databaseconnection.Database()
    db_obj.connect()
    cur = db_obj.conn.cursor()
    cur.execute(sql)
    foodId = cur.fetchone()
    cur.close()
    db_obj.conn.commit()
    return foodId