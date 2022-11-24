import sys
from pprint import pprint
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject')
import requests
import json
import config

fooditem=input("enter")

# def fetch_fooditem(fooditem):
#     nutrients=['Protein']
#     if data['currentPage'] is not None:
#         food=data['foods']
#         # print(food)
#         # pprint(food['foodNutrients'])
#         x = [x for x in food['foodNutrients'][0] if x['nutrientName'] in nutrients]
#         # print(x)






#
# fooditem=input("enter")

response_API = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=" + config.key + "&query=")
print(response_API.status_code)
data = response_API.text
data = json.loads(data)
print(data)
# fetch_fooditem()

# def fetch_foodnutrients(fooditem):






# fetch_fooditem(fooditem)
if __name__ == '__main__':
    print('hi')
