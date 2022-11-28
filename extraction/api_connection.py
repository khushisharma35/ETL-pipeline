import sys
from pprint import pprint
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject')
import requests
import json
import config
from transform .data_preprocessing import food_data

def get_input(fooditem):
    try:
        response_API = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=" + config.key + "&query="+ fooditem)
        print(response_API.status_code)
        data = response_API.text
        data = json.loads(data)
        # print(data)
        if data['totalHits'] == 0:
            raise Exception
        food_data(data,fooditem)
    except Exception as e :
        print(e)



if __name__ == '__main__':
    print('hi')
