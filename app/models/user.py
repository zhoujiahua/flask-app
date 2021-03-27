#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# Sqlalchemy
# Flask SQLalchemy
# wtforms
# flask_wtforms

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    description = Column(String(200))
    email = Column(String(20), nullable=False, unique=True)
    phone = Column(String(14))
    address = Column(String(50))

    def sample(self):
        pass
