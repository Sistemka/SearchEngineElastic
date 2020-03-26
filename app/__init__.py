from flask import Flask
from flask_restx import Api
from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

from config import Config
from app.main.routes import image_api
from app.errors.handlers import errors_api


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(
        app,
        doc='/swagger-ui'
    )

    api.add_namespace(image_api)
    api.add_namespace(errors_api)

    elastic_url = app.config.get('ELASTIC_URL')
    if elastic_url:
        app.elastic = Elasticsearch([elastic_url])
    else:
        app.elastic = Elasticsearch()

    searcher = SignatureES(es=app.elastic)
    app.searcher = searcher

    return app
