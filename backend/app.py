from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # App configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Enable CORS
    CORS(app)

    # Import blueprints (IMPORTANT: import inside function)
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.attendance_routes import attendance_bp
    from routes.leave_routes import leave_bp
    from routes.payroll_routes import payroll_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(attendance_bp, url_prefix="/api/attendance")
    app.register_blueprint(leave_bp, url_prefix="/api/leaves")
    app.register_blueprint(payroll_bp, url_prefix="/api/payroll")

    @app.route("/")
    def index():
        return {"message": "Dayflow HRMS Backend is running 🚀"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
