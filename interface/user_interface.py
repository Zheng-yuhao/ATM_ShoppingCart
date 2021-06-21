# 对于用户层的一些主要核心逻辑代码

from db import db_handler


# 用户注册功能核心代码
def register_interface(user_name,user_pass,balance = 15000):
    # 这里调用db_handler的select函数匹配src传入的值是否在db.txt文件中出现过
    re = db_handler.select(user_name)

    if re:
        return False, f'{user_name}已存在'

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
    # 用户通过了重名检验,所以创建了一个新用户的dict用于保存 → 接下来调用db_handler中的save函数保存文件
    db_handler.save(user_name,dic)
    return True, f'{user_name}注册成功'

def login_interface(user_name,user_pass):
    hash_re = db_handler.get_hash_lib(user_pass)
    re = db_handler.select(user_name)
    if not re:
        return False, f'用户名{[user_name]}或秘密输入错误,请重新输入'

    if hash_re == re.get('password'):
        return True, f'用户名{[user_name]}登录成功'

