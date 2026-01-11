from flask import Blueprint, request, jsonify
import time
import hmac

auth_bp = Blueprint("auth", __name__)

USERS = {
    "user@example.com": {
        "password": "password123"
    }
}

OTP_STORE = {}  # email -> {otp, expires_at, used}

OTP_TTL = 60  # seconds
MAX_ATTEMPTS = 5
ATTEMPTS = {}  # ip -> count
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = USERS.get(email)

    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    otp = "123456"  # static for lab, logic matters
    OTP_STORE[email] = {
        "otp": otp,
        "expires_at": time.time() + OTP_TTL,
        "used": False
    }

    return jsonify({"message": "Login OK, OTP issued"}), 200
@auth_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.json
    email = data.get("email")
    otp_input = data.get("otp")
    ip = request.remote_addr

    # Rate limiting
    ATTEMPTS[ip] = ATTEMPTS.get(ip, 0) + 1
    if ATTEMPTS[ip] > MAX_ATTEMPTS:
        return jsonify({"error": "Too many attempts"}), 429

    record = OTP_STORE.get(email)
    if not record:
        return jsonify({"error": "Invalid OTP"}), 401

    if record["used"] or time.time() > record["expires_at"]:
        return jsonify({"error": "OTP expired"}), 401

    if not hmac.compare_digest(record["otp"], otp_input):
        return jsonify({"error": "Invalid OTP"}), 401

    record["used"] = True
    ATTEMPTS[ip] = 0

    return jsonify({"message": "OTP verified"}), 200
