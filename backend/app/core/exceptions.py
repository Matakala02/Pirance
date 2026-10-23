class AppError(Exception):
    status_code = 400
    error = "bad_request"
    message = "Bad request"


class DuplicateUserError(AppError):
    status_code = 409
    error = "duplicate_user"
    message = "An account with this email or phone number already exists"
class InvalidCredentialsError(AppError):
    status_code = 401
    error = "invalid_credentials"
    message = "Incorrect email, phone number or password"


class NotAuthenticatedError(AppError):
    status_code = 401
    error = "not_authenticated"
    message = "Please log in to continue"