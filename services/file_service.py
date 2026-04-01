import os
from config.settings import STORAGE_DIR
from flask import send_from_directory, abort
from werkzeug.utils import secure_filename
from config.settings import MAX_FILE_SIZE
from logs.logger import logger
from flask import session

os.makedirs(STORAGE_DIR, exist_ok=True)

def save_file(file):
    filename = secure_filename(file.filename)

    if not filename:
        logger.warning("Upload failed: empty filename")
        return False

    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)

    if size > MAX_FILE_SIZE:
        logger.warning(f"Upload rejected (too large): {filename}")
        return False

    file_path = os.path.join(STORAGE_DIR, filename)
    file.save(file_path)

    logger.info(f"File uploaded: {filename} ({size} bytes)")
    return True


def list_files():
    return os.listdir(STORAGE_DIR)

def get_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(STORAGE_DIR, filename)

    if not os.path.exists(file_path):
        logger.warning(f"Download failed (not found): {filename}")
        abort(404)

    logger.info(f"File downloaded: {filename}")
    return send_from_directory(STORAGE_DIR, filename, as_attachment=True)


def save_file(file):
    filename = secure_filename(file.filename)

    if not filename:
        return False

    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)

    if size > MAX_FILE_SIZE:
        return False

    file_path = os.path.join(STORAGE_DIR, filename)
    file.save(file_path)
    return True

def delete_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(STORAGE_DIR, filename)

    if not os.path.exists(file_path):
        logger.warning(f"Delete failed (not found): {filename}")
        return False

    os.remove(file_path)
    logger.info(f"File deleted: {filename}")
    return True

