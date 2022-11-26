import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

dataset_path="/config/workspace/aps_failure_training_set1.csv"
database_name="aps"
collectin_name="sensor"

if __name__=="__main__":
    df =pd.read_csv(dataset_path)
    print(df.shape)

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[database_name][collectin_name].insert_many(json_record)