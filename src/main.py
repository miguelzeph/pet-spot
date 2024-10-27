from flask import Flask
from flask_app.views import flask_app
from settings import config_flask

app = Flask(
    __name__,
    template_folder="./flask_app/templates",
    static_folder="./flask_app/static"
)

# Registering Features
app.register_blueprint(flask_app)

# Configuration
# Flask
config_flask(app)

