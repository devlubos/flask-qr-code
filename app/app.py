from flask import Flask, render_template, request, flash, Blueprint


main_app = Blueprint('main_app', __name__)


@main_app.route("/")
def index():
    return render_template("index.html")


@main_app.route("/qr")
def qr():

    return render_template("qr.html")