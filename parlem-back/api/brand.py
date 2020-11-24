from business import BrandBusiness
from flask import abort, Blueprint, jsonify, request

blueprint = Blueprint('brand', __name__)
business = BrandBusiness()

@blueprint.route('/api/brand/all', methods=['GET'])
def api_get_all_brands():
    return jsonify(business.get_all_brands(True))

@blueprint.route('/api/brand', methods=['GET'])
def api_get_brand_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        return jsonify(business.get_brand_by_id(id, True))
    else:
        abort(400, "Error: The request argument 'id' was not provided.")