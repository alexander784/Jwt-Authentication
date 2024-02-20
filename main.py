from flask import Flask
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
    
  

    return app
