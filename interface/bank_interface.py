"""
bank interface
"""

from db import db_handler


def check_balance_interface(user_name):
    from db import db_handler
    re = db_handler.select(user_name)
    balance_re = re.get('balance')
    return f'Account[{user_name}]balance :{balance_re}'


def withdraw_balance_interface(user_name,money):
    from db import db_handler
    re = db_handler.select(user_name)
    balance_re = int(re.get('balance'))
    adj_money = int(money) * 1.05

    if balance_re >= adj_money:
        balance_re -= adj_money
        re['balance'] = balance_re

        db_handler.save(user_name,re)

        return True, f'Account[{user_name}],withdrawal successfully:{money}$,the commission is:{adj_money - int(money)}$'
    return False, f'Out of the limitation, please check your account.'


def repay_interface(user_name,money):
    from db import db_handler
    user_dict = db_handler.select(user_name)
    user_balance = user_dict.get('balance')
    user_balance += int(money)

    user_dict['balance'] = user_balance
    db_handler.save(user_name,user_dict)
    return True, f'Account:[{user_name}],charge successfully {money}$'


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

        return True, f'Account[{user}],TargetAccount[{target}],The amount to be transferred:{money}$,successfully'
    return False, f'Error,Out of the limitation, please check your account.'


def check_flow_interface(login_user):
    flow_list = db_handler.select(login_user)
    return flow_list.get('flow')


def pay_interface(login_user, cost):
    user_data = db_handler.select(login_user)
    if cost > user_data.get('balance'):
        return False
    user_data['balance'] -= cost

    flow = f'Deduction:[{cost}]$'
    user_data['flow'].append(flow)
    db_handler.save(login_user,user_data)
    return True