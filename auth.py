from flask import Blueprint,jsonify


##Blue print name
auth_Bp = Blueprint("auth", __name__)

##Endpoints
##Routes
@auth_Bp.post('/register')
def register_user():
    return jsonify({"message":"User created"})

