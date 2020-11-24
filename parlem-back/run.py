import flask
from flask import request, jsonify
from api import brand, customer, product


if __name__ == "__main__":
    app = flask.Flask(__name__)
    app.config["DEBUG"] = False
    app.register_blueprint(brand.blueprint) # Registers the 'Brand' blueprint and its API routes.
    app.register_blueprint(customer.blueprint) # Registers the 'Customer' blueprint and its API routes.
    app.register_blueprint(product.blueprint) # Registers the 'Product' blueprint and its API routes.
    app.run()