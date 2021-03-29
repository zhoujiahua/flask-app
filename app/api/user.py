#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from app.models.user import User
from . import api_user
from sqlalchemy.orm import session


@api_user.route("/api/user/login")
def api_user_login():
    # add_user = User()
    # add_user.name = 'jerry'
    # add_user.password = '123456'
    # add_user.email = 'jerry.zhou@advantest.com'
    # session.add(add_user)
    # session.commit()
    return 'user login api'


@api_user.route("/api/user/register")
def api_user_register():
    return 'user register api'
