#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app,supports_credentials=True)
    # app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    # Web register
    from app.web.user import web_user
    from app.web.home import web_home
    app.register_blueprint(web_user)
    app.register_blueprint(web_home)

    # Api register
    from app.api.user import api_user
    from app.api.comm import api_comm
    app.register_blueprint(api_user)
    app.register_blueprint(api_comm)

    

    
