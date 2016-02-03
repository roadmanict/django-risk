class CORSMiddleware(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = ("Content-Type, "
                                                    "Authorization")
        response['Access-Control-Allow-Methods'] = ("POST, GET, PUT, PATCH, "
                                                    "OPTIONS, DELETE")
        return response
