from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api import views
    app.register_blueprint(views, url_prefix='/')

    return app