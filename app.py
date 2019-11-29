from flask import Flask, render_template,request,redirect,url_for,jsonify,session,flash # For flask implementation
from bson import ObjectId # For ObjectId to work
import os
import datetime
import pandas as pd
import numpy as np

from bson.json_util import dumps
import json

import hashlib
from werkzeug import secure_filename
import mysql

mysqldb = mysql.Database()

import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='admin@mridayaitservices.com',
    toaddrs=['tapanb@mridayaitservices.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'csv'])

app = Flask(__name__)
app.secret_key = "spoogle" 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
title = "Floor Object Detection"
heading = "Floor Object Detection"

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')
           
@app.route("/")
def index():
	return render_template('index.html', title = 'Facility Mgmt Web application') 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def md5(password):
    if password:
        result = hashlib.md5(password.encode()).hexdigest()
        return result

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if 'admin' not in session: 
        if request.method == 'GET':
            return render_template('index.html')
        
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password'] 

            mysqldb.cur.execute("SELECT * FROM admin_details WHERE username = '"+username+"' and password = md5('"+password+"') LIMIT 1")
            result = mysqldb.cur.fetchall()
            
            if result:
                session['admin'] = 'admin'
                return redirect("/admin/home", code=302)
            else:
                flash('Username and Password is Wrong', 'danger')  
                return render_template('index.html')
    else:
        return redirect("/admin/home", code=302)

@app.route('/admin/logout')  
def admin_logout():  
    if 'admin' in session:  
        session.pop('admin',None)
        flash('You were successfully logout', 'success')        
        return redirect("/", code=302) 
    else:  
        return redirect("/", code=302)            

@app.route("/admin/home")
def admin_home():
    if 'admin' in session: 
        return render_template('admin/index.html', title = 'Dashboard')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')
 
@app.route("/admin/map")
def admin_map():
    if 'admin' in session: 
        return render_template('admin/map.html', title = 'Map')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')

@app.route("/admin/road_streetview")
def admin_road_streetview():
    if 'admin' in session: 
        return render_template('admin/road_streetview.html', title = 'Road Streetview')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')
        
@app.route("/admin/top_view")
def admin_top_view():
    if 'admin' in session: 
        return render_template('admin/top_view.html', title = 'Road Streetview')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')

@app.route("/admin/map-master")
def admin_map_master():
    if 'admin' in session: 
        return render_template('admin/top_view.html', title = 'Map Master')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')
        
@app.route("/admin/floor-master")
def admin_floor_master():
    if 'admin' in session: 
        return render_template('admin/top_view.html', title = 'Floor Master')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')

@app.route("/admin/object-detection")
def admin_object_detection():
    if 'admin' in session: 
        return render_template('admin/tensorflow.html', title = 'Object Detection')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')

@app.route("/admin/matterport")
@app.route("/admin/matterport/<id>")
def admin_matterport(id=None):
    if 'admin' in session:
        if(id):
            
            mysqldb.cur.execute("SELECT * FROM matterport_tags WHERE id = '"+id+"'")
            result = mysqldb.cur.fetchone()
            print(id)
            print(result)
        
            return render_template('admin/matterport_object.html', title = 'Matterport', res = result)
        else:
            return render_template('admin/matterport.html', title = 'Matterport')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')
        
@app.route("/admin/3d-object")
def admin_3d_object():
    if 'admin' in session: 
        return render_template('admin/3d-object.html', title = 'Object Detection')
    else:
        flash('Please login first', 'warning') 
        return render_template('index.html')

if __name__ == "__main__":

    app.run()
