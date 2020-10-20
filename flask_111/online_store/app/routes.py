#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: specifies http routes"""

from app import app
from flask import g, request, Flask, render_template
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
            # return out
            return render_template(
                "base.html",
                first_name = out["body"][0].get("first_name"),
                last_name = out["body"][0].get("last_name"),
                hobbies = out["body"][0].get("hobbies")
            )
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


        
@app.route("/sample1")
def sample1():
    return "<h1>Hello, World!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s!</h1>" % name

@app.route("/square/<int:number>")
def square(number):
    return("<h1>%s squared is %s</h1>"
    % (number, number**2))

@app.route("/countdown/<int:number>")
def countdown(number):
    return "</br>".join([str(i) for i in range(number, 0 , -1)])


@app.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent

# @app.route("/myroute")
# def my_view_function():
#     return render_template("index.html")

# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html", name=name)



key_id = "id"
key_name = "name"
key_category = "category"
key_price = "price"
key_stock = "stock"
key_image = "image"

def register_product(data):
    msg = "ok"
    # print("data ", str(data)
    try:
        command = "INSERT INTO product values(?,?,?,?,?,?)"
        cursor = get_db().execute(command, data)
        cursor.close()
        get_db().commit()
    except Exception as e:
        print(str(e))
        msg = str(e)
    return msg
    
@app.route("/products/register", methods=["GET", "POST"])
def registration_products():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        data = {
            key_id: request.form.get(key_id),
            key_name: request.form.get(key_name),
            key_category: request.form.get(key_category),
            key_price: request.form.get(key_price, 0, float),
            key_stock: request.form.get(key_stock, 0, int),
            key_image: request.form.get(key_image)
        }
        information = list(data.values())
        status = register_product(information)
        response = {
            "status": status,
            "data": information
        } 
        str_response = json.dumps(response)
        return render_template("register.html", data=str_response)


def get_all_products():
    cursor = get_db().execute("select * from product", ())
    results = cursor.fetchall()
    cursor.close()
    return results
def get_product(id):
    cursor = get_db().execute("SELECT * FROM product WHERE id=?", (id,))
    results = cursor.fetchall()
    cursor.close()
    return results

def update_product(data):
    msg = "updated"
    info = (data[key_name], data[key_category], data[key_price], data[key_stock], data[key_image], data[key_id])
    try:
        cursor = get_db().execute("UPDATE product SET name=?, category=?, price=?, stock=?, image=? WHERE id=?", info)
        get_db().commit()
        cursor.close()
        get_db().commit()
    except Exception as e:
        msg = str(e)
    return msg

def delete_product(id):
    msg = "ok"
    try:
        command = "DELETE FROM product WHERE id=?"
        cursor = get_db().execute(command, (id,))
        get_db().commit()
        cursor.close()
        get_db().commit()
    except Exception as e:
        msg = str(e)
    return msg    

def get_products_response():
    out = {"status": "ok", "body": ""}
    raw_data = get_all_products()
    if(len(raw_data) and raw_data is not str and len(raw_data) > 0):
        body_list = []
        for item in raw_data:
            temp_dic = {
                key_id: item[0],
                key_name: item[1],
                key_category: item[2],
                key_price: item[3],
                key_stock: item[4],
                key_image: item[5]
            }
            body_list.append(temp_dic)
        out["body"] = body_list
    else:
        out["status"] = "empty"
    return out
        

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        out_response = get_products_response()
        str_response = json.dumps(out_response)
        return render_template("products.html", data=str_response)
    if request.method == "POST":
        if (request.args.get("method", None, str) == "PUT"):
            data = {
                key_id: request.form.get(key_id),
                key_name: request.form.get(key_name),
                key_category: request.form.get(key_category),
                key_price: request.form.get(key_price, 0, float),
                key_stock: request.form.get(key_stock, 0, int),
                key_image: request.form.get(key_image)
            }
            status = update_product(data)
            print(str(status))
            if(status == "updated"):
                out_response = get_products_response()
                str_response = json.dumps(out_response)
                print(out_response)
                return render_template("products.html", data=str_response)
            else:
                information = list(data.values())
                response = {
                    "status": status,
                    "data": information
                } 
                str_response = json.dumps(response)
                return render_template("update.html", data=str_response)

        elif (request.args.get("method", None, str) == "CHANGE"):
            raw_data = get_product(request.form.get(key_id))
            if(len(raw_data) and raw_data is not str and len(raw_data) > 0):
                response = {
                    "status": "ok",
                    "data": list(raw_data[0])
                } 
                str_response = json.dumps(response)
                return render_template("update.html", data=str_response)
        elif (request.args.get("method", None, str) == "DELETE"):
            result = delete_product(request.form.get(key_id))
            out_response = get_products_response()
            if result != "ok":
                out_response["status"] = result
            str_response = json.dumps(out_response)
            return render_template("products.html", data=str_response)
        else:
            out_response = get_products_response()
            str_response = json.dumps(out_response)
            return render_template("products.html", data=str_response)

def register_in_cart(data):
    msg = "ok"
    # print("data ", str(data)
    try:
        command = "INSERT INTO shipping values(?,?)"
        cursor = get_db().execute(command, data)
        cursor.close()
        get_db().commit()
    except Exception as e:
        print(str(e))
        msg = str(e)
    return msg

def get_all_cart_products():
    cursor = get_db().execute("select * from shipping", ())
    results = cursor.fetchall()
    cursor.close()
    return results

@app.route("/catalog", methods=["GET", "POST"])
def catalog():
    if request.method == "GET":
        out_response = get_products_response()
        str_response = json.dumps(out_response)
        return render_template("catalog.html", data=str_response)
    if request.method == "POST":
        if (request.args.get("method", None, str) == "DETAILS"):
            raw_data = get_product(request.form.get(key_id))
            item = raw_data[0]
            temp_dic = {
                key_id: item[0],
                key_name: item[1],
                key_category: item[2],
                key_price: item[3],
                key_stock: item[4],
                key_image: item[5]
            }
            str_json = json.dumps(temp_dic)
            return render_template("details.html",data=str_json)