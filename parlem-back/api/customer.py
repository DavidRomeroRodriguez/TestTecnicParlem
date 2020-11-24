from business import CustomerBusiness
from flask import Blueprint, jsonify, request

blueprint = Blueprint('customer', __name__)
business = CustomerBusiness()

@blueprint.route('/api/customer/all', methods=['GET'])
def api_get_all_customers():
    return jsonify(business.get_all_customers(True))

@blueprint.route('/api/customer', methods=['GET'])
def api_get_customer_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        return jsonify(business.get_customer_by_id(id, True))
    else:
        return "Error: The request argument 'id' was not provided."