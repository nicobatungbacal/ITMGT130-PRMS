import database as db
from flask import session

def change_pass():
    old_password = {}
    old_password.setdefault("password",session["user"]["password"])

    new_password = {}
    new_password.setdefault()



    old_password = session["password"]

    db.change_password(old_password,new_password)
