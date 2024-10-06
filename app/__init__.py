from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    # Import and register the route blueprint
    from .routes import main
    app.register_blueprint(main)

    return app

# from flask import Flask
# from .routes import main

# def create_app():
#     app = Flask(__name__, template_folder='templates')
    
#     # Registre o blueprint
#     app.register_blueprint(main)
    
#     return app
