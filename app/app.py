from flask import render_template, request, Blueprint, make_response
import json

main_app = Blueprint('main_app', __name__)

@main_app.route("/", methods=["GET", "POST"])
def index():
    recent_values = get_recent_values()
    url = "https://www.google.com"
        
    response = make_response(render_template("index.html", url_link=url, recent_values=recent_values))
    response.set_cookie("recent_values", json.dumps(recent_values))
    return response


@main_app.route('/qrcode', methods = ["GET"])
def qrcode():
    recent_values = get_recent_values()
    url = request.args.get('url')

    recent_values = upload_recent_values(url, recent_values)
    
    response = make_response(render_template("index.html", url_link=url, recent_values=recent_values))
    response.set_cookie("recent_values", json.dumps(recent_values))
    return response


def get_recent_values():
    cookie_data = request.cookies.get("recent_values")
    return json.loads(cookie_data) if cookie_data else []


def upload_recent_values(url, recent_values):
    if url:
        recent_values.append(url)
        return recent_values[-10:]   
    return recent_values