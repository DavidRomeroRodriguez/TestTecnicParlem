import flask
from flask import request, jsonify
from api import brand, customer, product

app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.register_blueprint(brand.blueprint)
app.register_blueprint(customer.blueprint)
app.register_blueprint(product.blueprint)
app.run()