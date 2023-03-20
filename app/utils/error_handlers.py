from contextlib import contextmanager

from aiohttp.web import HTTPBadRequest
from pydantic.error_wrappers import ValidationError


@contextmanager
def raise_400_for_validation_error():
    try:
        yield
    except ValidationError as e:
        raise HTTPBadRequest(body=e.json())
