from business import ProductBusiness
from flask import Blueprint, jsonify, request

blueprint = Blueprint('product', __name__)
business = ProductBusiness()

@blueprint.route('/api/product/all', methods=['GET'])
def api_get_all_products():
    return jsonify(business.get_all_products(True))

@blueprint.route('/api/product', methods=['GET'])
def api_get_product_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        return jsonify(business.get_product_by_id(id, True))
    else:
        return "Error: The request argument 'id' was not provided."