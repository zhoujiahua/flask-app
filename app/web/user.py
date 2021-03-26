#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import jsonify
from . import web_user

@web_user.route("/user/login")
def web_user_login():
    return jsonify({"name": "jerry"})
