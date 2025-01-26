from flask import Flask
from app.v1 import conversations, logs, text_chat, vision_chat, upload, users

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(conversations.bp, url_prefix='/api/v1')
app.register_blueprint(logs.bp, url_prefix='/api/v1')
app.register_blueprint(text_chat.bp, url_prefix='/api/v1')
app.register_blueprint(vision_chat.bp, url_prefix='/api/v1')
app.register_blueprint(upload.bp, url_prefix='/api/v1')
app.register_blueprint(users.bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
