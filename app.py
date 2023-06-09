from flask import Flask, render_template, request, redirect, url_for, make_response
import logging
from tinydb import TinyDB, Query
import hashlib
import os
from dummy_camera_service import capture_image
from door_service import get_door_pin_status
from temperature_service import read_temp
from motion_service import get_motion_pin_status
import json
from flask_socketio import SocketIO, emit
from flask_cors import CORS


app = Flask(__name__)
#socketio = SocketIO(app, cors_allowed_origins=['*'])
#socketio = SocketIO(app, cors_allowed_origins=['http://127.0.0.1:5000']) 
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

db = TinyDB('db.json')
CAMERA_FOLDER = os.path.join('static', 'camera')
app.config['CAMERA_FOLDER'] = CAMERA_FOLDER
latest_camera_capture = os.path.join(app.config['CAMERA_FOLDER'], 'latest.jpg')


@app.route('/')
def index():
    app.logger.info('Inside default endpoint')
    
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    app.logger.info('Inside register')
    if request.method == 'POST':
        app.logger.info('Inside register - new user')
        username = request.form['username']
        password = request.form['password']

        app.logger.info('Inside register - saving new user')  
        db.insert({'username': username, 'password': hashlib.md5(password.encode()).hexdigest(), 'role': 'USER'})
        app.logger.info('Inside register - saving new user completed')  

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.info('Inside login')
    if request.method == 'POST':
        app.logger.info('Inside login - verifying credentials')
        username = request.form['username']
        password = request.form['password']
        app.logger.info('username %s' % username)

        user = Query()
        matching_users= db.search(user.username == username )
        
        if matching_users:
            app.logger.info(f'Found {matching_users}')
            logged_in_user=matching_users[0]
            app.logger.info(f'logged in user {logged_in_user}')

            if hashlib.md5(password.encode()).hexdigest() == logged_in_user["password"]:
                app.logger.info(f'password match')
                #return redirect(url_for('dashboard'))
                return render_template('dashboard2.html', loggedInUser=username) 
                #return render_template('dashboard.html', capture_image_path = latest_camera_capture)
            else:
                app.logger.info(f'password doesn\'t match')
                return render_template('login.html', error='Invalid password') 
        else:
            app.logger.warn(f'No users Found')
            return render_template('login.html', error='Invalid username')
        
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    app.logger.info('Inside Logout')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    app.logger.info('Inside dashboard')
    app.logger.info(f'capture_image_path = {latest_camera_capture}')
    
    return render_template('dashboard2.html')

@app.route('/motion', methods=['GET', 'POST'])
def motion():
    app.logger.info('Inside motion')    
    response = make_response(render_template('motion-detection.html'))
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #return render_template('motion-detection.html')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@socketio.on('connect')
def test_connect():
     app.logger.info('Inside test_connect')    
     socketio.emit('after connect', {'data':'Let us learn Web Socket in Flask'})

@app.route('/camera/capture', methods=['GET', 'POST'])
def camera_capture():
    app.logger.info ("camera_capture")
    return  capture_image()

@app.route('/door/status', methods=['GET', 'POST'])
def door_status():
    app.logger.info ("door_status")
    return str(get_door_pin_status())

@app.route('/temperature/status', methods=['GET', 'POST'])
def temperature_status():
    app.logger.info ("temperature_status")
    return json.dumps(read_temp())

@app.route('/motion/status', methods=['GET', 'POST'])
def motion_status():
    app.logger.info ("motion_status")
    return str(get_motion_pin_status())

#app.run(host='0.0.0.0', port=8081, debug=True)
socketio.run(app, host='0.0.0.0', port=8081, debug=True)