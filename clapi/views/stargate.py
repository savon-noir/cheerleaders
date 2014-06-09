from flask import Blueprint, make_response, jsonify, request, json

appmodule = Blueprint('stargate', __name__, url_prefix='/api/stargate')


@appmodule.route('/')
def index():
    return make_response(jsonify({}), 204)


@appmodule.route('/register', methods=['POST'])
def register():
    name = ''
    if not request.json or not 'name' in request.json:
        rcode = 400
    else:
        name = request.json['name']
        rcode = 200
    print request.json
    return make_response(jsonify(dict(name=name)), rcode)
