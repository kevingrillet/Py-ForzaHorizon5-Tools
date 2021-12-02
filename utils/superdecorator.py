import time
from functools import wraps

from utils import common
from utils.constant import DebugLevel
from utils.handlertime import HandlerTime


def print_on_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is__init__ = func.__qualname__.find('__init__') != -1
        name = func.__qualname__.replace('.__init__', '') if is__init__ else func.__qualname__
        debugLevel = DebugLevel.CLASS if is__init__ else DebugLevel.FUNCTIONS
        my_args = list(filter(lambda x: not hasattr(x, '__dict__'), args))
        common.debug('{} {}{}'.format(
            name,
            'created' if is__init__ else 'called',
            ' [{}{}{}]'.format('args: {}'.format(my_args) if my_args else '',
                               ', ' if my_args and kwargs else '',
                               'kwargs: {}'.format(kwargs) if kwargs else ''
                               ) if my_args or kwargs else ''), debugLevel)
        start_time = time.time()
        res = ''
        try:
            res = func(*args, **kwargs)
        finally:
            if not is__init__:
                common.debug(
                    '{} finished in {}{}'.format(name,
                                                 HandlerTime.handle_stringify(time.time() - start_time),
                                                 ' [return: {}]'.format(str(res)) if (res is not None) else ''),
                    debugLevel)
        return res

    return wrapper


def decorate_all_functions(function_decorator=print_on_call):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                try:
                    obj = obj.__func__  # unwrap Python 2 unbound method
                except AttributeError:
                    pass  # not needed in Python 3
                setattr(cls, name, function_decorator(obj))
        return cls

    return decorator
