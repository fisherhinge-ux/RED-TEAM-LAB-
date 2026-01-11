from flask import Flask
from auth import auth_bp
from reset import reset_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"

app.register_blueprint(auth_bp)
app.register_blueprint(reset_bp)

if __name__ == "__main__":
    app.run(debug=True)
