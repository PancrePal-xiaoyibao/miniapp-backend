# app/v1/conversations.py
from flask import Blueprint, jsonify

bp = Blueprint('conversations', __name__)

@bp.route('/conversations', methods=['GET'])
def get_conversations():
    """
    获取对话列表
    """
    conversations = [
        {"id": 1, "title": "Conversation 1"},
        {"id": 2, "title": "Conversation 2"},
    ]
    return jsonify(conversations)

@bp.route('/conversations/<int:conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """
    获取指定ID的对话
    """
    conversation = {"id": conversation_id, "title": f"Conversation {conversation_id}"}
    return jsonify(conversation)


@bp.route('/conversations', methods=['POST'])
def create_conversation():
    """
    创建新的对话
    """
    # 这里可以添加处理请求数据的逻辑，例如解析 JSON
    return jsonify({"message": "Conversation created"}), 201
