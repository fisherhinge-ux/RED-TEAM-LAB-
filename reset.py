from flask import Blueprint, request, jsonify
import uuid

reset_bp = Blueprint("reset", __name__)
RESET_TOKENS = {}

@reset_bp.route("/request-reset", methods=["POST"])
def request_reset():
    email = request.json.get("email")
    token = str(uuid.uuid4())
    RESET_TOKENS[token] = email
    return jsonify({"reset_token": token})


@reset_bp.route("/reset-password", methods=["POST"])
def reset_password():
    token = request.json.get("token")

    if token in RESET_TOKENS:
        return jsonify({"message": "Password reset successful"})

    return jsonify({"error": "Invalid token"}), 400
