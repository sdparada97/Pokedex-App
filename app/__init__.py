from flask import Flask

from app.config.config import config_dict

from app.routes.main import main

def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Register blueprints
    app.register_blueprint(main)
    
    return app