from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"

@auth.route('/register')
def register():
    return "<p>Register</p>"