'''
数据处理定义
'''
import os
import json
from conf import settings


# 判断用户名是否已经存在于db.txt中
def select(user_name):
    USER_DATA_PATH = os.path.join(settings.DB_PATH,'user_data',f'{user_name}.json')
    if os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, mode = 'r', encoding = 'utf-8') as f:
            user_dict = json.load(f)
            return user_dict


# save功能,要求写活,给每一个用户分别创建一个json格式的文件,内容就是user_interface中定义的dict
def save(user_name,dic):
    USER_DATA_PATH = os.path.join(settings.DB_PATH,'user_data',f'{user_name}.json')
    with open(USER_DATA_PATH, mode = 'w',encoding = 'utf-8') as f:
        json.dump(dic,f,ensure_ascii = False)

# 给用户密码加盐的函数
def get_hash_lib(password):
    import hashlib
    m = hashlib.md5()
    m.update('密码加盐start'.encode('utf-8'))
    m.update(password.encode('utf-8'))
    m.update('密码加盐end'.encode('utf-8'))
    return m.hexdigest()