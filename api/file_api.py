from flask import Blueprint, jsonify
from services.file_service import list_files
from auth.decorators import login_required
from flask import request
from services.file_service import save_file
from services.file_service import delete_file

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/files", methods=["GET"])
@login_required
def api_list_files():
    files = list_files()
    return jsonify({
        "status": "success",
        "count": len(files),
        "files": files
    })

@api_bp.route("/upload", methods=["POST"])
@login_required
def api_upload_file():
    file = request.files.get("file")

    if not file:
        return jsonify({"status": "error", "message": "No file provided"}), 400

    success = save_file(file)

    if not success:
        return jsonify({"status": "error", "message": "Upload failed"}), 400

    return jsonify({"status": "success", "message": "File uploaded"})

@api_bp.route("/delete/<filename>", methods=["DELETE"])
@login_required
def api_delete_file(filename):
    success = delete_file(filename)

    if not success:
        return jsonify({"status": "error", "message": "File not found"}), 404

    return jsonify({"status": "success", "message": "File deleted"})
