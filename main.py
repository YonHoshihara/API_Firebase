from flask import Flask
from database import start_database_conection, get_user_status, deactive_user_conection, active_user_concection, \
    add_new_user, get_all_user
import json

ref = start_database_conection()
app = Flask(__name__)

@app.route("/login/<userId>")
def login(userId):
    user_status = get_user_status(ref, userId)
    response = {"success": False}
    if user_status:
        active_user_concection(ref,userId)
        response['success'] = True
        response = json.dumps(response)
        return response
    else:
        response['success'] = False
        response = json.dumps(response)
        return response

@app.route("/logoff/<userId>")
def logoff(userId):
    user_status = deactive_user_conection(ref, userId)
    response = {"success": False}
    if(user_status):
        response['success'] = True
        response = json.dumps(response)
        return response
    else:
        response['success'] = False
        response = json.dumps(response)
        return response

@app.route("/register/<userId>")
def register(userId):

    register = add_new_user(ref, userId)
    response = {"success": False}

    if register:
        response['success'] = True
        response = json.dumps(response)
        return response
    else:
        response['success'] = False
        response = json.dumps(response)
        return response

@app.route("/get_all")
def get_all():

    all_users = get_all_user(ref)
    response = {"success": False}

    if all_users:
        response['success'] = True
        response['data'] = all_users
        response = json.dumps(response)
        return response
    else:
        response['success'] = False
        response = json.dumps(response)
        return response


if __name__ == '__main__':

    app.run()

