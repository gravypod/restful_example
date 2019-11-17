from flask import Flask
from restful_example.routes import routes

__all__ = ['app']

app = Flask(__name__)
app.register_blueprint(routes)
