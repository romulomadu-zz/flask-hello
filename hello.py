import os
from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return 'username is {:}'.format(request.values["username"])
  return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'


if __name__ == '__main__':
  host = os.getenv('IP','0.0.0.0')
  port = int(os.getenv('PORT', 5000))
  app.debug = True
  app.run(host=host, port=port)
  #app.run()