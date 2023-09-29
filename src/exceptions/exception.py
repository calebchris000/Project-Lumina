import typing as t
from fastapi import HTTPException, status


class NotFoundError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "data not found",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_404_NOT_FOUND,
        )


class AccessDenied(HTTPException):
    def __init__(
        self,
        detail: t.Any = "Sorry, you do not have the necessary permissions to access this resource",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_403_FORBIDDEN,
        )


class InvalidParameterError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "Invalid parameter",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )


class ForbiddenError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "data not found",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_403_FORBIDDEN,
        )


class UnauthorizedError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "Authentication failed",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class DuplicateError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "data already exists",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_409_CONFLICT,
        )


class BadDataError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "Account has been already verified",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_400_BAD_REQUEST,
        )


class ServerError(HTTPException):
    def __init__(
        self,
        detail: t.Any = "Error performing request, please try again",
        headers: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(
            detail=detail,
            headers=headers,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
