from flask import Flask

def create_app():
    app = Flask(__name__)

    from .socketio import socketio

    socketio.init_app(app)

    return app