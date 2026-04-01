from flask import Blueprint, render_template
from auth.decorators import login_required
from services.stats_service import get_storage_stats, parse_logs

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    storage = get_storage_stats()
    uploads, downloads, deletes, activity = parse_logs()

    return render_template(
        "dashboard.html",
        storage=storage,
        uploads=uploads,
        downloads=downloads,
        deletes=deletes,
        activity=activity
    )
