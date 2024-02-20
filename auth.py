from flask import Blueprint,jsonify,request
from models import User


##Blue print name
auth_Bp = Blueprint("auth", __name__)

##Endpoints
##Routes
@auth_Bp.post('/register')
def register_user():

    data = request.get_json()

    user = User.get_user_by_username(username= data.get('username'))

    if User is not None:
        return jsonify({"error":"User Already exists"}),403
    new_user = User(
        username = data.get('username'),
        email = data.get('email')
    )

    new_user.set_password(password= data.get('password'))

    ##SAve user
    new_user.save()


    return jsonify({"message":"User created"}),201

