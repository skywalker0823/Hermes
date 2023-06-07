from flask import Flask, redirect

def create_app():
    app = Flask(__name__)

    from .socketio import socketio

    socketio.init_app(app)

    # DB
    # from .models.db import db
    # db.init_app(app)

    # Blueprints
    from .views.home import home
    from .views.message import message

    blueprint_list = [
        {"blueprint": home, "url_prefix": "/home"},
        {"blueprint": message, "url_prefix": "/message"}
    ]

    for blueprint in blueprint_list:
        app.register_blueprint(blueprint["blueprint"], url_prefix=blueprint["url_prefix"])

    @app.route("/")
    def index():
        return redirect("/home")

    return app