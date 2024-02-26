from flask import Flask,jsonify
from extensions import db,jwt
from auth import auth_Bp
from users import user_bp



def create_app():

    app = Flask(__name__)

    ##COnfigure app
    app.config.from_prefixed_env()
##INitialize exts
    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprint
    app.register_blueprint(auth_Bp, url_prefix='/auth')
    app.register_blueprint(user_bp,url_prefix='/users')

    #jwt error handler

    @jwt.exxpired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify ({"message":"Token has expired", "error":"token expired"})

    
  

    return app
