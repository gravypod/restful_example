from flask import Blueprint, jsonify, request

from restful_example.models import Thing
from restful_example.registry import ThingRegistry

routes = Blueprint(__name__, 'routes')
thing_registry = ThingRegistry()


@routes.route('/healthz', methods=['GET'])
def healthz():
    return '', 200


@routes.route('/readyz', methods=['GET'])
def readyz():
    return '', 200


@routes.route('/things', methods=['GET'])
def thing_list():
    return jsonify([
        thing.to_dict()
        for thing in thing_registry.list()
    ])


@routes.route('/things/<thing_id>', methods=['GET'])
def thing_get(thing_id: str):
    return jsonify(thing_registry.get(thing_id).to_dict())


@routes.route('/things', methods=['POST'])
def thing_create():
    return jsonify(thing_registry.create(Thing.from_dict(request.json)).to_dict())


@routes.route('/things/<thing_id>', methods=['PUT'])
def thing_update(thing_id: str):
    return jsonify(thing_registry.update(request.json, thing_registry.get(thing_id)).to_dict())


@routes.route('/things/<thing_id>', methods=['DELETE'])
def thing_delete(thing_id: str):
    return jsonify(thing_registry.delete(thing_registry.get(thing_id)))


@routes.route('/things/<thing_id>', methods=['DELETE'])
def thing_exists(thing_id: str):
    thing_registry.get(thing_id)
    return '', 200
