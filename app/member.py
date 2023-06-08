from flask import Blueprint, request, session, redirect, url_for, render_template as rt
import json

member = Blueprint("Member", __name__)





@member.route("/test", methods=["GET", "POST"])
def login():
    data = {"test": "test_success"}
    return json.dumps(data)