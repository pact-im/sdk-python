class ApiCallException(Exception):
    pass


class FileNotFoundException(Exception):
    pass


class InvalidArgumentException(Exception):
    pass


class ApiCallHttpError(ApiCallException):
    code: int
    message: str

    def __init__(self, message: str = None) -> None:
        super().__init__(message or '%s: %s' % (self.code, self.message))


class PactBadRequest(ApiCallHttpError):
    code = 400
    message = 'Bad Request – Your request sucks'


class PactUnauthorized(ApiCallHttpError):
    code = 401
    message = 'Unauthorized – Your API key is wrong'


class PactPaymentRequired(ApiCallHttpError):
    code = 402
    message = 'Payment Required – Paywoll enabled for the company, you must pay before doing API requests'


class PactForbidden(ApiCallHttpError):
    code = 403
    message = 'Forbidden – The endpoint is unavailable for you'


class PactNotFound(ApiCallHttpError):
    code = 404
    message = 'Not Found – The specified resource could not be found'


class PactMethodNotAllowed(ApiCallHttpError):
    code = 405
    message = 'Method Not Allowed – You tried to access with an invalid method'


class PactNotAcceptable(ApiCallHttpError):
    code = 406
    message = 'Not Acceptable – You requested a format that isn’t json'


class PactGone(ApiCallHttpError):
    code = 410
    message = 'Gone – The requested resource has been removed from our servers'


class PactTooManyRequests(ApiCallHttpError):
    code = 429
    message = 'Too Many Requests – You’re requesting too many requests! Slow down!'


class PactInternalServerError(ApiCallHttpError):
    code = 500
    message = 'Internal Server Error – We had a problem with our server. Try again later.'


class PactBadGateway(ApiCallHttpError):
    code = 502
    message = 'Bad Gateway – We’re temporarially offline for maintanance. Please try again later.'


class PactServiceUnavailable(ApiCallHttpError):
    code = 503
    message = 'Service Unavailable – We’re temporarially offline for maintanance. Please try again later.'


class IAmTeapot(ApiCallHttpError):
    code = 418
    message = 'I’m a teapot'


ERRORS_MAP = (
    (400, PactBadRequest),
    (401, PactUnauthorized),
    (402, PactPaymentRequired),
    (403, PactForbidden),
    (404, PactNotFound),
    (405, PactMethodNotAllowed),
    (406, PactNotAcceptable),
    (410, PactGone),
    (418, IAmTeapot),
    (429, PactTooManyRequests),
    (500, PactInternalServerError),
    (502, PactBadGateway),
    (503, PactServiceUnavailable),
)


def http_error_handler(status_code: int):
    error = dict(ERRORS_MAP).get(status_code)
    if not error:
        return ApiCallException('Api returned HTTP non-OK status: %s' % status_code)
    return error()
