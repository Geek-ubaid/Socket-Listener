from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO,send,emit

import socket
import hashlib
import struct
import os
import listener
import socket

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html', error=error)
    else:
        return redirect(url_for('home'))
    

@app.route('/ws', methods=['GET', 'POST'])
def websocket():
    global sock
    listener.server_program(sock)   
    return "ok"	

@app.route('/restart', methods=['GET', 'POST'])
def reboot():
    return "restarted"

@socketio.on('client_connected')
def handle_client_connect_event(json):
    print(str(json))
    emit('response',200)
   
    
@socketio.on('disconnect')
def disconnected():
    print('disconnected')
    
@socketio.on('connect')
def connected():
    print('connected')
    

if __name__ == "__main__":
    socketio.run(app,debug=True,port=3000)
    
        
