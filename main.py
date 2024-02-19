from flask import Flask
from extensions import db
from auth import auth_Bp



def create_app():

    app = Flask(__name__)

    ##COnfigure app
    app.config.from_prefixed_env()
##INitialize exts
    db.init_app(app)

    # Register Blueprint
    app.register_blueprint(auth_Bp, url_prefix='/auth')
    
    
  

    return app
