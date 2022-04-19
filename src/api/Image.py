import os

import PIL
from flask import send_file
from flask_restful import Resource
from resizeimage import resizeimage


class Image(Resource):

    HOME = ""

    def __init__(self):
        from server import cfg
        self.HOME = cfg['imghome']

    def get(self, path):
        path = path.replace(' ', '%20')
        obrazok = os.path.join(self.HOME, path)
        ext = os.path.splitext(obrazok)[1]
        return send_file(obrazok, mimetype='image/' + ext[1:])