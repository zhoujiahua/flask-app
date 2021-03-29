#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from app.models.user import User, db
from . import api_user


@api_user.route("/api/user/login")
def api_user_login():
    users = {
        'name': 'jerry',
        'description': 'how do you see',
        'password': '123456',
        'email': 'jerry.zhou@advantest.com',
        'phone': '110',
        'address': 'China'
    }
    # add_user = User()
    # add_user.name = 'jerry'
    # add_user.password = '123456'
    # add_user.email = 'jerry.zhou@advantest.com'
    # session.add(add_user)
    # session.commit()
    # db.session.add(add_user)
    # db.session.commit()

    return 'user login api'


@api_user.route("/api/user/register")
def api_user_register():
    return 'user register api'
