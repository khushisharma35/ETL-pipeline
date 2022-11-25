import sys
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject/')
from extraction .api_connection import data,fooditem
from load import databaseconnection
from transform .data_preprocessing import required_nutrientsid
from transform import data_preprocessing
from transform .data_preprocessing import nutrientsidname

def insert_food(fooditem,id,description,category):
    sql= f"""insert into food_item values('{fooditem}',{id},'{description}','{category}')"""
    print("h")
    db_obj = databaseconnection.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)
    return sql
# def insert_nutrients(id,name):
#     for nutrientsidname in required_nutrientsid:
#
#     sql = f"""insert into nutrients values({id},'{name}')"""
#     print("haaa")
#     db_obj = databaseconnection.Database()
#     db_obj.connect()
#     db_obj.insert_rows(sql)
#     return sql
# def insert_food_nutrients_mapping():
#     sql=""" insert into food_nutrients_mapping values"""

