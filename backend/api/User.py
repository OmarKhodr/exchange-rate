from flask import request, jsonify, abort, Blueprint, Response
from app import db, bcrypt
from api.helper import create_token, decode_token, extract_auth_token
from models.User import User, UserSchema
from sqlalchemy import not_


user_schema = UserSchema()

users_schema = UserSchema(many = True)

app_user = Blueprint('app_user', __name__)


@app_user.route('/user', methods = ['POST'])
def add_user():
    """ Creates/Signs up a User
    ---
    parameters:
      - name: user_name
        in: body
        type : string
        example: HusseinJaber20
        required: true
      - name: password
        in: body
        type : string
        example: Arsenal123
        required: true
    responses:
      200:
        description: The user_name and the user's id as a json

      400:
        description : The input is invalid. Make sure you have passed user_name and password.
    """

    user_name = request.json.get('user_name')
    password = request.json.get('password')
    if user_name and password:
        new_User = User(
            user_name = user_name,
            password = password
        )
        db.session.add(new_User)
        db.session.commit()
        return jsonify(user_schema.dump(new_User))
    return Response("{ 'Message' : 'Invalid Input :(' }", status=400, mimetype='application/json')


#Get the user_names of all users in the database
@app_user.route('/users', methods = ['GET'])
def get_users():
    """ Returns all users registered
    ---
    parameters:
      - name: token
        in: header
        type : string
        required: true
        description : The token returned by the backend whenever a certain user signs in. The token is a hashed string of the user's id
    responses:
      200:
        description: A json of all users registered

    """
    token = extract_auth_token(request)
    user_id = decode_token(token)
    users = User.query.with_entities(User.user_name, User.id)
    res = []
    for user in users:
        if user.id == user_id:
            continue
        res.append(user)
    return jsonify(users_schema.dump(res))

#Authenticate a User
@app_user.route('/authentication', methods = ['POST'])
def authenticate_user():
    """ Authenticates user's credentials. Used when a user wants to sign in.
    ---
    parameters:
      - name: user_name
        in: body
        type : string
        example: HusseinJaber20
        required: true
      - name: password
        in: body
        type : string
        example: Arsenal123
        required: true
    responses:
      200:
        description: A token, to be used later by the user. A token is a hashed string of the user's id.
      400:
        description : The input is invalid. Make sure you have passed the correct user_name and password.
    """
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    if user_name and password:
        user = User.query.filter_by(user_name = user_name).first()
        if(user is None):
            return Response("{ 'Message' : 'Invalid Username :(' }", status=403, mimetype='application/json')
        same_password = bcrypt.check_password_hash(user.hashed_password,password)
        if(same_password is False):
            return Response("{ 'Message' : 'Invalid Password :(' }", status=403, mimetype='application/json')
        
        # User is indeed valid, return a jwt token
        Token = create_token(user.id)
        return jsonify (
            token = Token   
        )