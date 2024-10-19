from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url = 'mongodb+srv://Siddhesh:MukruROxpwIPnuvj@cluster0.wqxco.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

#create a new client and connectt to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME="siddhesh"
COLLECTION_NAME='waferproject'

df=pd.read_csv("C:\Users\ACER\Downloads\Sensor Project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)