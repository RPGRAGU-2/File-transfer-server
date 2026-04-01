from flask import Blueprint, render_template, request, redirect, url_for
from services.file_service import save_file, list_files
from services.file_service import get_file
from services.file_service import delete_file
from auth.decorators import login_required

file_bp = Blueprint("files", __name__)

@file_bp.route("/")
@login_required
def index():
    files = list_files()
    return render_template("index.html", files=files)

@file_bp.route("/upload", methods=["POST"])
@login_required
def upload():
    files = request.files.getlist("files")

    for file in files:
        if file:
            save_file(file)

    return redirect(url_for("files.index"))


@file_bp.route("/download/<filename>")
@login_required
def download(filename):
    return get_file(filename)

@file_bp.route("/delete/<filename>", methods=["POST"])
@login_required
def delete(filename):
    delete_file(filename)
    return redirect(url_for("files.index"))

