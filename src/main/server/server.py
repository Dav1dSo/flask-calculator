from flask import Flask
from src.main.routes.calculators import calculators_bp

app = Flask(__name__)

Blueprints = [
    calculators_bp
]

for i in Blueprints:
    app.register_blueprint(i)
    