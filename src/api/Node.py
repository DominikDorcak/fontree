from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.trees.DBNode import DBNode


class Node(Resource):

    def get(self,id):
        json = {}
        try:
            node = DBNode(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['node'] = node.jsonify()
        return json, 200


