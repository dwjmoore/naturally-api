from flask import jsonify, session

def logout():
    session.pop("email", None)
    session.pop("user_type", None)
    return jsonify({"msg": "User is logged out"}), 200