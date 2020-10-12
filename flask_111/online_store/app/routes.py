#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: specifies http routes"""

from app import app
@app.route('/')
def index():
    return "Hello, World!\n"

@app.route('/aboutme')
def aboutme():
    dic = {
        "firts_name":"Ivan",
        "last_name":"Ramirez",
        "hobby":"watch tv :p"
    }
    return str(dic) + "\n"