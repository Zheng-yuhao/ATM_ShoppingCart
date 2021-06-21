from db import db_handler

# 关于银行相关的接口
def check_balance_interface(user_name):

    from db import db_handler
    re = db_handler.select(user_name)
    balance_re = re.get('balance')
    return f'用户名{user_name}的账户余额为{balance_re}'

# 银行取款接口
def withdraw_balance_interface(user_name,money):
    from db import db_handler
    re = db_handler.select(user_name)
    balance_re = int(re.get('balance'))
    adj_money =  int(money) * 1.05 # 加上手续费后的取出金额

    if balance_re >= adj_money:
        balance_re -= adj_money # 这一步只是改了balance_re的值,并没有直接改变re(返回的是dict)中balance的值
        re['balance'] = balance_re

        db_handler.save(user_name,re)

        return True, f'用户名{user_name},成功提款{money}元,手续费为{adj_money - int(money)}'
    return False, f'提现金额不够,穷鬼,赶紧死开吧'

# 银行充值接口
def repay_interface(user_name,money):
    from db import db_handler
    user_dict = db_handler.select(user_name)
    user_balance = user_dict.get('balance')
    user_balance += int(money)

    user_dict['balance'] = user_balance
    db_handler.save(user_name,user_dict)
    return True, f'用户名:{user_name}成功充值{money}元'

# 银行转账接口
def transfer_interface(user,target,money):
    from db import db_handler
    user_dict = db_handler.select(user)
    target_dict = db_handler.select(target)
    if target_dict and user_dict['balance'] >= int(money):

        user_balance = user_dict.get('balance')
        target_balance = target_dict.get('balance')

        user_balance -= int(money)
        target_balance += int(money)

        user_dict['balance'] = user_balance
        target_dict['balance'] = target_balance

        db_handler.save(user,user_dict)
        db_handler.save(target,target_dict)

        return True, f'用户{user}给用户{target}进行了转账{money}元的操作,成功'
    return False, f'用户不存在或balance不够,请用户检查账户或检查对象用户名'

# 银行流水查询接口
def check_flow_interface(login_user):
    flow_list = db_handler.select(login_user)
    return flow_list.get('flow')

# 支付功能
def pay_interface(login_user, cost):
    user_data = db_handler.select(login_user)
    if cost > user_data.get('balance'):
        return False
    user_data['balance'] -= cost

    flow = f'用户消费金额:[{cost}]'
    user_data['flow'].append(flow)
    db_handler.save(login_user,user_data)
    return True