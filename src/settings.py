import os
from klein_config import get_config

config = get_config()


# Constants Flask
UPLOAD_FOLDER = config.get("flask.upload_folder")
SECRET_KEY = config.get("flask.secret_key")
SESSION_TYPE = config.get("flask.session_type")
FLASK_DEBUG = config.get("flask.debug")
# Constants TensorFlow
CUDA_VISIBLE_DEVICES = config.get("tensorflow.cuda_visible_devices")
MODEL_PATH = config.get("tensorflow.model_path")


def config_flask(app):
    """Setup Flask environment variables

    Args:
        app : The flask object
    """
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SESSION_TYPE"] = SESSION_TYPE
    app.config["FLASK_DEBUG"] = str(FLASK_DEBUG)
    # os.environ["FLASK_DEBUG"] = str(FLASK_DEBUG)

def config_tensorflow():
    os.environ["CUDA_VISIBLE_DEVICES"] = str(CUDA_VISIBLE_DEVICES)
    os.environ["MODEL_PATH"] = MODEL_PATH