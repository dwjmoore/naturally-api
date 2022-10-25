from flask import jsonify, session

def admin():
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401
    
    return jsonify({"msg": "You are an authorized user for admin privileges."}), 200