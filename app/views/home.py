from flask import Blueprint, request, session, redirect, url_for, render_template as rt
from datetime import datetime, timezone

home = Blueprint("Home", __name__, template_folder="templates")

@home.route("/")
def index():
    return rt('home.html')

# 處理登入與註冊
@home.route("/", methods=["POST"])
def home_post():
    return None