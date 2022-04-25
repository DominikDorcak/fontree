
import yaml
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.api.ExperimentEntry import ExperimentEntry
from src.api.RandomFont import RandomFont
from src.api.Font import Font
from src.api.Image import Image
from src.api.Node import Node
from src.api.Question import Question
from src.api.Status import Status

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from src import config

app = Flask(__name__)
cfg = yaml.safe_load(pkg_resources.read_text(config, 'config.yaml'))
cors = CORS(app)


api = Api(app)
api.add_resource(Status, '/')
api.add_resource(Image, '/image/<path:path>')
api.add_resource(Node, '/node/<int:id>')
api.add_resource(Font, '/font/<int:id>')
api.add_resource(RandomFont, '/font/random')
api.add_resource(Question, '/question/<int:id>')
api.add_resource(ExperimentEntry, '/experiment/entry')







