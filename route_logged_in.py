from flask import jsonify, session

def logged_in():
    email = session.get("email")
    
    if not email:
        return jsonify({"logged_in": False}), 200
    
    return jsonify({"logged_in": True}), 200