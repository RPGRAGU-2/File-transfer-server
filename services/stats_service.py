import os
from config.settings import STORAGE_DIR

LOG_FILE = "logs/server.log"

def get_storage_stats():
    total_size = 0
    file_count = 0

    for file in os.listdir(STORAGE_DIR):
        path = os.path.join(STORAGE_DIR, file)
        if os.path.isfile(path):
            file_count += 1
            total_size += os.path.getsize(path)

    return {
        "file_count": file_count,
        "total_size": total_size
    }

def parse_logs():
    uploads = downloads = deletes = 0
    recent_activity = []

    if not os.path.exists(LOG_FILE):
        return uploads, downloads, deletes, recent_activity

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    for line in lines[-20:]:  # recent 20 events
        recent_activity.append(line.strip())

        if "uploaded" in line:
            uploads += 1
        elif "downloaded" in line:
            downloads += 1
        elif "deleted" in line:
            deletes += 1

    return uploads, downloads, deletes, recent_activity
