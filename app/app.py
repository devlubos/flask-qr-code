from flask import render_template, request, Blueprint, make_response
import json

main_app = Blueprint('main_app', __name__)


@main_app.route("/", methods=["GET", "POST"])
def index():

    cookie_data = request.cookies.get("recent_values")
    if cookie_data:
        recent_values = json.loads(cookie_data)
    else:
        recent_values = []

    if request.method == "POST":
        url = request.form["url"]
        if url:
            recent_values.append(url)
            recent_values = recent_values[-10:]        
    else:
        url = "https://www.google.com"

    response = make_response(render_template("index.html", url_link=url, recent_values=recent_values))
    response.set_cookie("recent_values", json.dumps(recent_values))
    return response