from flask import jsonify, session

def admin():
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"auth": False}), 200
    if user_type != 1980:
        return jsonify({"auth": False}), 200
    
    return jsonify({"auth": True}), 200