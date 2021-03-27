#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=8000, debug=True)
