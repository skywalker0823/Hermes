from flask import Blueprint, request, session, redirect, url_for, render_template as rt
from datetime import datetime, timezone

message = Blueprint("Message", __name__, template_folder="templates")

@message.route("/")
def index():
    return rt('message.html')