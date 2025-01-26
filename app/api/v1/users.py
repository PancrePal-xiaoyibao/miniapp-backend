# app/v1/users.py
from flask import Blueprint, jsonify

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    """
    获取用户列表
    """
    users = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"},
    ]
    return jsonify(users)


@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    获取指定ID的用户信息
    """
    user = {"id": user_id, "name": f"User {user_id}"}
    return jsonify(user)

@bp.route('/users', methods=['POST'])
def create_user():
    """
    创建新用户
    """
    # 这里可以添加处理请求数据的逻辑，例如解析 JSON
    return jsonify({"message": "User created"}), 201
