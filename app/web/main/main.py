#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import render_template
from . import web_main


@web_main.route('/')
def main_index():
    return render_template('main/index.html')
