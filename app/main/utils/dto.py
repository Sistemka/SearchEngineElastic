from flask_restx import Namespace, reqparse
from werkzeug.datastructures import FileStorage


basic_args = reqparse.RequestParser(bundle_errors=True, trim=True)
basic_args.add_argument('X-SERVICE-NAME', location='headers', required=True, nullable=False)


class ImageDto:
    api = Namespace(
        'image', description='all handlers to process images in SearchEngine', validate=True
    )
    image = reqparse.RequestParser(bundle_errors=True, trim=True)
    image.add_argument('image', type=FileStorage, location='files', required=True, action='append')

    image_path = reqparse.RequestParser(bundle_errors=True, trim=True)
    image_path.add_argument('image_path', type=str, location='args', required=True)


class ErrorsDto:
    api = Namespace(
        '', description='all error handlers', validate=True
    )
