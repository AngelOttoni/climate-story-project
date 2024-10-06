from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    # Import and register the route blueprint
    from .routes import main
    app.register_blueprint(main)

    return app