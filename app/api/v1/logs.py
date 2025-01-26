# app/v1/logs.py
from flask import Blueprint, jsonify

bp = Blueprint('logs', __name__)

@bp.route('/logs', methods=['GET'])
def get_logs():
    """
    获取日志列表
    """
    logs = [
        {"id": 1, "message": "Log message 1"},
        {"id": 2, "message": "Log message 2"},
    ]
    return jsonify(logs)

@bp.route('/logs/<int:log_id>', methods=['GET'])
def get_log(log_id):
  """
  获取指定ID的日志
  """
  log = {"id": log_id, "message": f"Log message {log_id}"}
  return jsonify(log)

