from flask import Flask, request, jsonify


app = Flask(__name__)

#In-memory user dictionary
users_dict = {}
user_id = 0

#Add data for users_dict
def initialize_users():
    global user_id
    init_users = [
        {
            "username": "stevewillson",
            "password": "sw125689",
            "t_fullname": "Steve John Willson",
            "t_birthdate": "2012-02-03",
            "t_phone": "0526547890",
            "p_fullname": "John Fade Willson",
            "p_contact": "0504655897",
        },
        {
            "username": "katedoe",
            "password": "kk078dd",
            "t_fullname": "Kate Dan Doe",
            "t_birthdate": "2010-05-10",
            "t_phone": "0527700112",
            "p_fullname": "Dan Joe Doe",
            "p_contact": "0548869364",
        }
    ]
# Create user
#get data ,create user ,return json of user 
@app.route('/users', methods=['POST'])
def create_user():
    return jsonify("user"), 201

# Read user by ID
#get id, return json of user  
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify("user"), 200


# Update user
#get id and date , update user, return new json user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    
    return jsonify("new user"), 200

# Delete user
#get id, delete user, return message 
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'User deleted'
