from src import app
from flask import request, jsonify, abort
from src.db import Service

@app.route("/user/<userid>")
def get_user(userid):
    _db = Service()
    user_data = _db.get_entitled_perms_by_user_id(userid)
    return jsonify(user_data)

@app.route("/checkpermission")
def checkpermission():
    user_id = request.args.get('userid', None)
    perm_id = request.args.get('permissionid', None)
    
    if not user_id or not perm_id:
        abort(400)
    _db = Service()
    user_data = _db.user_with_permission_exists(user_id, perm_id)
    return jsonify(user_data)

@app.route("/roles/<role_id>", methods=['POST'])
def modify_perms_in_role(role_id):
    if not role_id:
        abort(400)
    post_data = request.get_json()
    _db = Service()
    response = _db.modify_permission_of_role(role_id, post_data['permissions'])
    return jsonify(response)

@app.route("/permissions/<permisson_id>", methods=['DELETE'])
def delete_permission(permisson_id):
    if not permisson_id:
        abort(400)
    _db = Service()
    response = _db.delete_permission(permisson_id)
    return jsonify(response)
