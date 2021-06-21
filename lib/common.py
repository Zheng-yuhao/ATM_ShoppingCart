'''
公用方法
'''
import logging.config
from conf import settings

# 装饰器构成
def outer(func):
    from core import src
    def inner(*args, **kwargs):
        if src.login_info is None:
            print('你还没登录呢!请登录哦!')
            src.login()

        res = func(*args, **kwargs)
        return res

    return inner

# 添加日志功能
def get_logger(log_type):
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    logger = logging.getLogger(log_type)
    return logger