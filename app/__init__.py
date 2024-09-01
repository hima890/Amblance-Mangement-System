from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

def create_app():
    # Create the flask app instance
    app = Flask(__name__)

    # Create the extionsions instances
    db = SQLAlchemy() # Database
    migrate = Migrate() # Migration

    # Initialize the app with the extensions
    db.init_app(app) # Database
    migrate.init_app(app, db) # Migration

    # Load the configuration
    app.config.from_object(Config)

    # Create the database and tables
    with app.app_context():
        import models
        db.create_all()

    # Regse5ter the views blueprints


    # Return the app instance after initialization
    return app
