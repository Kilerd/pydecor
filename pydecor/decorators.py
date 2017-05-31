"""
A module housing the decorators provided in the public API of PyDecor
"""

from logging import getLogger
from functools import partial, wraps
from types import FunctionType, MethodType
from typing import Callable, Union


__all__ = (
    'before',
)


log = getLogger(__name__)


DecoratorType = Union[FunctionType, MethodType, type]


def before(func, unpack_kwargs=True, **decorator_kwargs):
    """Specify a callable to be run before the decorated resource
    
    :param func: 
    :param unpack_kwargs:
    :param decorator_kwargs: 
    
    :return:
    """

    def decorator(decorated):
        """The function returned in place of the decorated function"""

        @wraps(decorated)
        def wrapper(*args, **kwargs):
            """The function called in place of the wrapped function"""
            if unpack_kwargs:
                ret = func(args, kwargs, **decorator_kwargs)
            else:
                ret = func(args, kwargs, decorator_kwargs=decorator_kwargs)

            return ret

        return wrapper

    return decorator
