import requests
from bs4 import BeautifulSoup
from load import insertdata


def get_url(fooditem):
    try:
        url= f"https://www.bbcgoodfood.com/search?q={fooditem}"
        page = requests.get(url)
        soup =BeautifulSoup(page.content,'html.parser')
        s = soup.findAll(attrs={'class': 'col-12 template-search-universal__card'})

        text = s[0].find_all('a')
        foodlink=text[0].get('href')
        baseurl = "https://www.bbcgoodfood.com"
        link = baseurl + foodlink

        recipelink = requests.get(link)
        recipecontent=BeautifulSoup(recipelink.content,'html.parser')
        get_recipe = recipecontent.findAll("li", class_="pb-xs pt-xs list-item")
        for val in get_recipe:
            val.text
            foodrecipe=val.text
            print(foodrecipe)
            insertdata.insert_recipe(fooditem,foodrecipe)





    except Exception as e:
        print(e)






