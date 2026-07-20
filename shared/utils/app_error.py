from typing import Optional


class AppError(Exception):
    """Custom application error with status code and detail message."""

    def __init__(self, status_code: int = 500, detail: str = "Internal Server Error"):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)


class NotFoundError(AppError):
    """Resource not found error."""

    def __init__(self, detail: str = "Data tidak ditemukan"):
        super().__init__(status_code=404, detail=detail)


class UnauthorizedError(AppError):
    """Authentication error."""

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=401, detail=detail)


class ForbiddenError(AppError):
    """Authorization error."""

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=403, detail=detail)


class ApiKeyInvalidError(AppError):
    """Invalid API key error."""

    def __init__(self, detail: str = "API KEY Invalid !"):
        super().__init__(status_code=403, detail=detail)


class ValidationError_(AppError):
    """Input validation error."""

    def __init__(self, detail: str = "Validation Error"):
        super().__init__(status_code=422, detail=detail)
