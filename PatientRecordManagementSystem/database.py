import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

prms_db = myclient["PRMS"]

def get_user(username):
    patients_coll = prms_db['patients']
    patient=patients_coll.find_one({"username":username})
    return patient

doctors =
    {10 : {"firstname":"Ernesto","lastname":"Celdran","Specialty":"X-Ray","start_time":ISODate("2021-05-31T10:00:00.000Z"),"end_time":ISODate("2021-05-31T17:00:00.000Z")}}
    {20 : {"firstname":"Maria","lastname":"Hechanova","Specialty":"Blood Chemistry","start_time":ISODate("2021-05-31T8:00:00.000Z"),"end_time":ISODate("2021-05-31T13:00:00.000Z")}}
    {30 : {"firstname":"Salvador","lastname":"Perez","Specialty":"CT Scan","start_time":ISODate("2021-05-31T11:00:00.000Z"),"end_time":ISODate("2021-05-31T19:00:00.000Z")}}
    {40 : {"firstname":"Teresa","lastname":"Galvez","Specialty":"Ultrasound","start_time":ISODate("2021-05-31T7:00:00.000Z"),"end_time":ISODate("2021-05-31T13:00:00.000Z")}}
    {40 : {"firstname":"Teresa","lastname":"Galvez","Specialty":"Pulmonology","start_time":ISODate("2021-05-31T9:00:00.000Z"),"end_time":ISODate("2021-05-31T18:00:00.000Z")}}
    {40 : {"firstname":"Teresa","lastname":"Galvez","Specialty":"Molecular Diagnostics","start_time":ISODate("2021-05-31T12:00:00.000Z"),"end_time":ISODate("2021-05-31T15:00:00.000Z")}}

def get_doctor(code):
    return doctors[code]

def get_doctors():
    doctor_list = []

    for i,v in doctors.items():
        doctor = v
        prod
