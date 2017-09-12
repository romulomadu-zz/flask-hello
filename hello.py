import os
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return url_for('show_user_profiles',username='romulomadu')

@app.route('/username/<username>')
def show_user_profiles(username):
  # show the user profile for that user
  return "User {:} visited".format(username)

@app.route('/hello')
def hello_world():
  return "Hello World"

@app.route('/post/<int:pos_id>')
def show_post(pos_id):
  return "Post {:}".format(pos_id)

if __name__ == '__main__':
  host = os.getenv('IP','0.0.0.0')
  port = int(os.getenv('PORT', 5000))
  app.debug = True
  app.run(host=host, port=port)
  #app.run()