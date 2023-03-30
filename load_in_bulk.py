import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.gj31nse.mongodb.net/test')
db = client['database name']
collection = db['collection name']

# I had 7 csv files 

for i in range(1, 8):
    # using pandas to read csv files.
    df = pd.read_csv(f'stocks{i}.csv')
    
    ### whatever cleaning you want to do on your data ###
    
    
    
    # Convert the DataFrame to a list of dictionaries
    records = df.to_dict(orient='records')
    
    # Notice insert_many is used to insert the data in bulk in short time period.
    collection.insert_many(records)
    print(f"Inserted documents", i)
        
client.close()