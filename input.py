from extraction import api_connection
import pandas as pd
from webScrapping import get_recipes



def user_input():
    csvdata=pd.read_csv('/Users/apple/PycharmProjects/etlproject/input.csv')
    for data in csvdata['foods']:
        fooditem =data
        api_connection.get_input(fooditem)
        get_recipes.get_url(fooditem)


    # return fooditem

    # api_connection.get_input(fooditem)