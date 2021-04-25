from werkzeug.wrappers import Request
from src.validate import schemas


class MiddleWare:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        schemas[request.path].validate(dict(request.form))

        return self.app(environ, start_response)
