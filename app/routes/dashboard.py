from flask import Blueprint, render_template, request
from app.models.predict import predict_resume
dashboard_bp = Blueprint("dashboard", __name__)
@dashboard_bp.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        resume = request.files["resume"]
        result = predict_resume(resume)
        return render_template(
            "dashboard_result.html",
            result=result
        )
    return render_template("dashboard.html")