"""
This is the entry point only to our api /
"""

# Load modules
from flask import jsonify
from shared.config import app

# API index entry point
@app.route("/", methods=["GET"])
def index():
    return jsonify({ "msg": "Workflow manager API : mini project" })