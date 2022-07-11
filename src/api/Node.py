from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.trees.DBNode import DBNode


class Node(Resource):

    def get(self,id):
        """
                Načítanie údajov o vrchole v strome
                ---
                        parameters:
                          - in: path
                            name: id
                            type: integer
                            required: true
                        responses:
                          200:
                            description: Node
                            schema:
                              id: Node
                              properties:
                                node:
                                  type: object
                                  properties:
                                    node_id:
                                      type: integer
                                      description: ID vrchola
                                    left_child:
                                      type: integer
                                      description: ID ľavého syna
                                    right_child:
                                      type: integer
                                      description: ID pravého syna
                                    font_id:
                                      type: integer
                                      description: ID výsledného fontu
                                    question_id:
                                      type: integer
                                      description: ID otázky v uzle
                                    is_leaf:
                                      type: boolean
                                      description: flag na identifikáciu listového vrcholu
                        """
        json = {}
        try:
            node = DBNode(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['node'] = node.jsonify()
        return json, 200


