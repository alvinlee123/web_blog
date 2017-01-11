from flask import request
from flask import session

from src.common.database import Database
from src.models.user import User

__author__ = 'alee'

from flask import Flask, render_template

app = Flask(__name__) # '__main__' private variable
app.secret_key = 'alvin'

@app.route('/') #www.mysite.com/api/

def hello_method():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email,password):
        User.login(email)

    return render_template("profile.html", email=session['email'])

if __name__ == '__main__':
    app.run(port=4995, debug= True)
