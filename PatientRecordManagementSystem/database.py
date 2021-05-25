import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

PRMS_db = myclient["PRMS"]
