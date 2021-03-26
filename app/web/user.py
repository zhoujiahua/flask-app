#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import jsonify
from . import user

@user.route("/user/login")
def user_login():
    return jsonify({"name": "jerry"})
