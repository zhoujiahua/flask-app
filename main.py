#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
import requests
import json
from app.utils.read_file import encode_base64, decode_base64, read_img, printosinfo

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Automatic script hook'


@app.route('/hook/test')
def hook_test():
    with open('./static/to.json','rb') as f:
        to_data = f.read()
        return to_data


if __name__ == '__main__':
    app.run(debug=True)
