from flask import Flask, render_template, request
import pickle
from flask_app.routes import main,result,bonus

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main.bp)
    app.register_blueprint(result.bp)
    app.register_blueprint(bonus.bp)
    return app
