from werkzeug.exceptions import HTTPException

from app.main.utils.dto import ErrorsDto

errors_api = ErrorsDto.api


@errors_api.errorhandler(HTTPException)
def http_exception(e):
    response = {
        'message': str(e),
        'error': True,
    }
    return response, getattr(e, 'code', 500)


@errors_api.errorhandler(Exception)
def application_exception(e):
    response = {
        'message': str(e),
        'error': True,
    }
    return response, getattr(e, 'code', 500)
