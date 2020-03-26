from io import BytesIO

from flask import jsonify, request, current_app, make_response
from flask_restx import Resource

from app.main.utils.dto import ImageDto, basic_args

image_api = ImageDto.api


@image_api.route('/add')
class ImageAdd(Resource):
    @image_api.expect(ImageDto.image, ImageDto.image_path, basic_args)
    @image_api.doc('add image to elastic')
    def post(self):
        basic_args.parse_args()
        # images = ImageDto.image.parse_args()
        image_path = ImageDto.image_path.parse_args()['image_path']

        count = 0
        for k in request.files:
            received_file = request.files[k]

            current_app.searcher.add_image(
                path=image_path,
                img=received_file.stream.read(),
                bytestream=True
            )
            count += 1

        message = f'{count} images successfully added'
        code = 200
        if count == 0:
            message = 'no images to add'
            code = 204
        return make_response(jsonify({
            'error': False,
            'message': message
        }), code)


@image_api.route('/search')
class ImageSearch(Resource):
    @image_api.expect(ImageDto.image, basic_args)
    @image_api.doc('search in elastic index for similar images')
    def post(self):
        basic_args.parse_args()

        result = []
        for k in request.files:
            received_file = request.files[k]
            result_for_image = [
                item['path'] for item in
                current_app.searcher.search_image(
                    path=received_file.stream.read(),
                    bytestream=True
                )
            ]
            result.append(result_for_image)

        return make_response(jsonify({
            'error': False,
            'result': result
        }), 200)
