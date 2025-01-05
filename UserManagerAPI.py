from flask import Flask, request, jsonify
import user

app = Flask(__name__)

#In-memory user dictionary
users_dict = {}
user_id_count = 0

#Add data for users_dict
def initialize_users():
    global user_id_count
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
        },
    ]
    for user_data in init_users:
        user_id_count += 1
        user1 = user.User(user_id_count, **user_data)
        users_dict[user_id_count] = user1

initialize_users()

# Create user
#get data ,create user ,return json of user 
@app.route('/users', methods=['POST'])
def create_user():
    global user_id_count
    data = request.get_json()
    if not data:
        return jsonify({'eror':'No input data provided'}),400

    user_id_count += 1
    user1 = user.User(
        user_id = user_id_count,
        username=data.get("username"),
        password=data.get("password"),
        t_fullname=data.get("t_fullname"),
        t_birthdate=data.get("t_birthdate"),
        t_phone=data.get("t_phone"),
        p_fullname=data.get("p_fullname"),
        p_contact=data.get("p_contact"),
    )
    users_dict[user_id_count] = user1
    return jsonify(user1.to_dict()), 201

# Read user by ID
#get id, return json of user  
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user1 = users_dict.get(user_id)
    if not user1:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user1.to_dict()), 200


# Update user
#get id and date , update user, return new json user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user1 = users_dict.get(user_id)
    if not user1:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'eror': 'No input data provided'}), 400

    #Updating user data
    user1.username = data.get("username", user1.username)
    user1.password = data.get("password", user1.password)
    user1.t_fullname = data.get("t_fullname", user1.t_fullname)
    user1.t_birthdate = data.get("t_birthdate", user1.t_birthdate)
    user1.t_phone = data.get("t_phone", user1.t_phone)
    user1.p_fullname = data.get("p_fullname", user1.p_fullname)
    user1.p_contact = data.get("p_contact", user1.p_contact)

    return jsonify(user1.to_dict()), 200


# Delete user
#get id, delete user, return message 
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user1 = users_dict.pop(user_id, None)
    if not user1:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User Deleted!'})

