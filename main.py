from flask import Flask, request, jsonify, g
import hashlib
import sqlite3
app = Flask(__name__)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db', check_same_thread=False)
        g.db.row_factory = sqlite3.Row
    return g.db
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
app.teardown_appcontext(close_db)
def delete(username,password):
    db=get_db()
    check=login_user(username,password)
    if 200 in check :
        db.execute(f"DELETE FROM users WHERE username = '{username}'")
        db.commit()
        return jsonify({"response":"account delete successfully "}),200
    else :
        return jsonify({"response ":"Bruh are you joking !"}) ,600
def add_user(username, password):
    db = get_db()
    password_hash = hash_password(password)
    try:
        db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        db.commit()
        return jsonify({"response": "User added successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"response": f"Username '{username}' already exists"}), 400
def login_user(username, password):
    db = get_db()
    password_hash = hash_password(password)
    cursor = db.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        stored_hash = result['password_hash']
        if password_hash == stored_hash:
            return jsonify({"response": "Login successful"}), 200
        else:
            return jsonify({"response": "Incorrect password"}), 401
    else:
        return jsonify({"response": "Username not found"}), 404
@app.route('/deleteaccount',methods=['POST'])
def accdelete():
    data= request.json
    username=data.get('username')
    password=data.get('password')
    if not username or not password :
        return jsonify({"response":"username or password are required "}),400
    return delete(username,password)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"response": "Username and password are required"}), 400
    return add_user(username, password)
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"response": "Username and password are required"}), 400
    return login_user(username, password)
if __name__ == '__main__':
    app.run(debug=True)