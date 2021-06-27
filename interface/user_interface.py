"""
user interface
"""

from db import db_handler


def register_interface(user_name,user_pass,balance = 15000):
    re = db_handler.select(user_name)

    if re:
        return False, f'{user_name} already exist.'

    dic = {
        'username':user_name,
        'password':user_pass,
        'balance':balance,
        'flow':[],
        'shop_car':[],
        'locked':False
    }
    # get_hash_lib()
    hash_re = db_handler.get_hash_lib(user_pass)
    dic['password'] = hash_re

    db_handler.save(user_name,dic)
    return True, f'{user_name}registration successfully!'

def login_interface(user_name,user_pass):
    hash_re = db_handler.get_hash_lib(user_pass)
    re = db_handler.select(user_name)
    if not re:
        return False, f'Account{[user_name]}type error,please re-enter your password.'

    if hash_re == re.get('password'):
        return True, f'Account{[user_name]} login successfully!'