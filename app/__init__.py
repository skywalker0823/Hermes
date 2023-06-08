from flask import Flask, redirect

# 使用遷移工具來更新資料庫 包含建立table
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from .socketio import socketio

    socketio.init_app(app)

    # DB
    from .models.db import db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    # 建立資料庫
    migrate.init_app(app, db)

    # Blueprints
    from .views.home import home
    from .views.message import message

    from .member import member

    blueprint_list = [
        {"blueprint": home, "url_prefix": "/home"},
        {"blueprint": message, "url_prefix": "/message"},
        {"blueprint": member, "url_prefix": "/api/member"},
    ]

    for blueprint in blueprint_list:
        app.register_blueprint(blueprint["blueprint"], url_prefix=blueprint["url_prefix"])

    @app.route("/")
    def index():
        return redirect("/home")

    return app