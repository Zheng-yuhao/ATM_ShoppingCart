'''
Common functions
'''
import logging.config
from conf import settings

# decorator
def outer(func):
    from core import src
    def inner(*args, **kwargs):
        if src.login_info is None:
            print('你还没登录呢!请登录哦!')
            src.login()

        res = func(*args, **kwargs)
        return res

    return inner

# log
def get_logger(log_type):
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    logger = logging.getLogger(log_type)
    return logger