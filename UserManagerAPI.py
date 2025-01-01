from flask import *

app = Flask(__name__)

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
