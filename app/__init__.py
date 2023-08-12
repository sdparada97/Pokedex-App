from flask import Flask
import logging

from app.config.config import config_dict

from app.routes.main import main

def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    app.config.from_object(config)

    # Set logging
    logging.basicConfig(level=logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')

    file_handler = logging.FileHandler('poke_app.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Configurar el manejador de consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Obtener el objeto logger raíz
    logger = logging.getLogger('')
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Register blueprints
    app.register_blueprint(main)
    
    return app