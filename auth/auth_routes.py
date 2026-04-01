from flask import Blueprint, render_template, request, redirect, url_for, session
from config.settings import ADMIN_USERNAME, ADMIN_PASSWORD

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["authenticated"] = True
            session["username"] = username
            return redirect(url_for("files.index"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

