import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STORAGE_DIR = os.path.join(BASE_DIR, "storage")
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
SECRET_KEY = "change-this-later"
ADMIN_USERNAME = "Ragu"
ADMIN_PASSWORD = "59905990"
