import os
from flask import Flask, url_for, request, render_template, redirect, flash, session
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
#app.config['SERVER_NAME']


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('username'),
                        request.form.get('password')):
            flash("Succesfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning('Incorrect username and password for user (%s)', request.form.get('username'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
      
if __name__ == '__main__':
  host = os.getenv('IP','0.0.0.0')
  port = int(os.getenv('PORT', 5000))
  app.debug = True
  app.secret_key = 's\xb4\xe7\x88H\xe9\xf8\x19\xe6\xe8=@\xcc\xeb\xa0\x84<|\xd1\xcd\x04V\x1b\xc5'
  # logging
  handler =  RotatingFileHandler('error.log', maxBytes=10000, backupCount=1) 
  handler.setLevel(logging.INFO)
  app.logger.addHandler(handler)
  app.run(host=host, port=port)
  
  #app.run()