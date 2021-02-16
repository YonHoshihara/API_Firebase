import firebase_admin
from firebase_admin import credentials, firestore, db

def start_database_conection():
    cred = credentials.Certificate("./android-e2335-firebase-adminsdk-sp7ul-2ce84f5ab7.json")
    default_app = firebase_admin.initialize_app(cred,
                                             {'databaseURL': 'https://android-e2335-default-rtdb.firebaseio.com/'})
    client = firestore.client()
    ref = db.reference('/')
    ref_child = ref.child('users')

    return ref_child

def add_new_user(ref_child,user_id):

    try:
        ref_child.update({user_id: {'conected': 0}})
        return True

    except Exception as ex:
        return False

def get_user_status(ref_child, user_id):
    ref = ref_child.child(str(user_id))
    response = ref.get()
    if response:
        return response
    else:
        return False

def get_all_user(ref_child):
    try:
        response = ref_child.get()
        return response
    except Exception as ex:
        return False

def update_user_status(ref_child, user_id, status):
    user_status = get_user_status(ref_child, user_id)
    if user_status:
        try:
            ref = ref_child.child(str(user_id))
            ref.update({"conected": status})
            return True
        except Exception as ex:
            return False

    else:
        return False

def active_user_concection(ref_child, user_id):

    response = update_user_status(ref_child, user_id, 1)
    if response:
        return response
    else:
        return False

def deactive_user_conection(ref_child, user_id):
    response = update_user_status(ref_child, user_id, 0)
    if response:
        return response
    else:
        return False


