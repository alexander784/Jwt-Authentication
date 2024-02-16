from flask import Flask



def create_app():

    app = Flask(__name__)

    ##COnfigure app
    app.config.from_prefixed_env()

    return app
