import pymongo

client = pymongo.MongoClient("mongodb+srv://Sarang2906:Pranali06@sarang-06.tcssiqv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Sarang",
    "email" : "sarangchandekar@gmail.com",
    "surname" : "Chandekar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
