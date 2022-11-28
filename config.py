import os
from os.path import join , dirname
from dotenv import load_dotenv


dotenv_path =join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

key= os.environ.get("apikey")
host=os.environ.get("host")
port=os.environ.get("port")
databaseName=os.environ.get("databaseName")
username=os.environ.get("username")
password=os.environ.get("password")

