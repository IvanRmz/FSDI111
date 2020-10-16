#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: specifies http routes"""

from app import app
from flask import g, request
import sqlite3
import json

DATABASE = "online_store"
first_name_key = "first_name"
last_name_key = "last_name"
hobbies_key = "hobbies"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_all_users():
    cursor = get_db().execute("select * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return results
def save_user(first_name, last_name, hobbies):
    msg = "user saved!"
    try:
        command = "insert into user values(?,?,?)"
        cursor = get_db().execute(command, (first_name, last_name, hobbies))
        cursor.close()
        get_db().commit()
    except Exception as e:
        msg = "Unexpected error: " + str(e)
    return msg + "\n"

def update_user(query_params, data_update):
    msg = "user updated!"
    try:
        command = "UPDATE user set "
        new_values = []
        conditions = []
        if (first_name_key in data_update and data_update[first_name_key] is not None):
            if(len(new_values) > 0):
                command += ", "
            command += (first_name_key + "=? ")
            new_values.append(data_update[first_name_key])
        if (last_name_key in data_update and data_update[last_name_key] is not None):
            if(len(new_values) > 0):
                command += ", "
            command += (last_name_key + "=? ")
            new_values.append(data_update[last_name_key])
        if (hobbies_key in data_update and data_update[hobbies_key] is not None) :
            if(len(new_values) > 0):
                command += ", "
            command += (hobbies_key + "=? ")
            new_values.append(data_update[hobbies_key])
            
        if(query_params[first_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += first_name_key + "=? "
            conditions.append(query_params[first_name_key])
        if(query_params[last_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += last_name_key + "=? "
            conditions.append(query_params[last_name_key])
        if(query_params[hobbies_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += hobbies_key + "=? "
            conditions.append(query_params[hobbies_key])
        params = tuple(new_values + conditions)
        print(command)
        print(str(params))

        cursor = get_db().execute(command, params)
        get_db().commit()
        cursor.close()
        get_db().commit()
    except Exception as e:
        msg = "Unexpected error: " + str(e)
    return msg + "\n"

def delete_user(query_params):
    msg = "user deleted!"
    try:
        command = "DELETE FROM user "
        conditions = []
        if(query_params[first_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += first_name_key + "=? "
            conditions.append(query_params[first_name_key])
        if(query_params[last_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += last_name_key + "=? "
            conditions.append(query_params[last_name_key])
        if(query_params[hobbies_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += hobbies_key + "=? "
            conditions.append(query_params[hobbies_key])
        params = tuple(conditions)
        print(command)
        print(str(params))

        cursor = get_db().execute(command, params)
        get_db().commit()
        cursor.close()
        get_db().commit()
    except Exception as e:
        msg = "Unexpected error: " + str(e)
    return msg + "\n"

def get_user_filter(query_params):
    msg = ""
    try:
        command = "SELECT * FROM user "
        conditions = []
        if(query_params[first_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += first_name_key + "=? "
            conditions.append(query_params[first_name_key])
        if(query_params[last_name_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += last_name_key + "=? "
            conditions.append(query_params[last_name_key])
        if(query_params[hobbies_key] is not None):
            if(not "WHERE" in command):
                command += " WHERE "
            if(len(conditions) > 0):
                command += "AND "
            command += hobbies_key + "=? "
            conditions.append(query_params[hobbies_key])
        params = tuple(conditions)
        print(command)
        print(str(params))

        cursor = get_db().execute(command, params)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as e:
        msg = "Unexpected error: " + str(e)
    return msg + "\n"
    
     


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


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

@app.route("/users", methods=["GET", "POST", "PUT", "DELETE"])
def get_users():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        first_name = request.args.get(first_name_key, None, str)
        last_name = request.args.get(last_name_key, None, str)
        hobbies = request.args.get(hobbies_key, None, str)
        if(first_name is not None or last_name is not None or hobbies is not None):
            query_params = { 
                first_name_key: first_name, 
                last_name_key: last_name,
                hobbies_key: hobbies
            }
            raw_data = get_user_filter(query_params)
        else :
            raw_data = get_all_users()
        if(raw_data is not str and len(raw_data) > 0):
            for item in raw_data:
                temp_dic = {
                    first_name_key: item[0],
                    last_name_key: item[1],
                    hobbies_key: item[2]
                }
                body_list.append(temp_dic)
            out["body"] = body_list
            return out
        else:
            return "No data found"
    if "POST" in request.method:
        first_name = request.args.get(first_name_key, None, str)
        last_name = request.args.get(last_name_key, None, str)
        hobbies = request.args.get(hobbies_key, None, str)
        if(first_name is None or last_name is None or hobbies is None):
            return "Please insert the 3 valid param in the url (first_name , last_name and hobbies)\n"
        else:
            return save_user(first_name, last_name, hobbies)
    if "PUT" in request.method:
        first_name = request.args.get(first_name_key, None, str)
        last_name = request.args.get(last_name_key, None, str)
        hobbies = request.args.get(hobbies_key, None, str)
        if(first_name is not None or last_name is not None or hobbies is not None):
            query_params = { 
                first_name_key: first_name, 
                last_name_key: last_name,
                hobbies_key: hobbies
            }
            try:
                s = request.data
                print(s)
                data_update = json.loads(s)
                return update_user(query_params, data_update)
            except:
                return "It is needed a string data body json with the information to update\n"
        else:
            return "It is needed at least one param in the URL (first_name , last_name , hobbies)\n"
    
    if "DELETE" in request.method:
        first_name = request.args.get(first_name_key, None, str)
        last_name = request.args.get(last_name_key, None, str)
        hobbies = request.args.get(hobbies_key, None, str)
        if(first_name is not None or last_name is not None or hobbies is not None):
            query_params = { 
                first_name_key: first_name, 
                last_name_key: last_name,
                hobbies_key: hobbies
            }
            return delete_user(query_params)
        else:
            return "It is needed at least one param in the URL (first_name , last_name , hobbies)\n"


        
        