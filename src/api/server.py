
import yaml
from flask import Flask, redirect, url_for
from flask_restful import Api
from flask_cors import CORS

from src.api.AllQuestions import AllQuestions
from src.api.ExperimentEntry import ExperimentEntry
from src.api.FontAnswer import FontAnswer
from src.api.RandomFont import RandomFont
from src.api.Font import Font
from src.api.Image import Image
from src.api.Node import Node
from src.api.Question import Question
from src.api.Status import Status
from flasgger import Swagger


try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from src import config

app = Flask(__name__)
cfg = yaml.safe_load(pkg_resources.read_text(config, 'config.yaml'))
cors = CORS(app)
template = {
  "swagger": "2.0",
  "info": {
    "title": "Fontree API",
    "description": "API pre web fontree.eu",
    "version": "1.0",
    "contact": {
      "name": "Dominik Dorčák",
      "url": "https://fontree.eu",
    }
  }
}

swagger = Swagger(app, template=template)

@app.route('/')
def hello():
    return redirect(url_for('flasgger.apidocs'))


api = Api(app)
api.add_resource(Status, '/status')
# api.add_resource(Image, '/image/<path:path>')
api.add_resource(Node, '/node/<int:id>')
api.add_resource(Font, '/font/<int:id>')
api.add_resource(RandomFont, '/font/random')
api.add_resource(FontAnswer, '/font/answer')
api.add_resource(Question, '/question/<int:id>')
api.add_resource(AllQuestions, '/question/all')
api.add_resource(ExperimentEntry, '/experiment/entry')








