'''
Business Logic layer
'''
from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common

login_info = None


# Register
def register():
    print('Registration function is being carried out >>>')
    while True:
        user_name = input('User id >>> : ').strip()
        user_pass = input('User Password >>> ： ').strip()
        re_user_pass = input('Re-enter the Password >>> : ').strip()

        if user_pass == re_user_pass:
            re, msg = user_interface.register_interface(user_name, user_pass)

            if re:
                print(msg)
                break
            else:
                print(msg)


# Login
def login():
    print('Login function is being carried out >>>')
    while True:
        user_name = input('User id >>> : ').strip()
        user_pass = input('User Password >>> ： ').strip()
        re, msg = user_interface.login_interface(user_name, user_pass)
        if not re:
            print(msg)
        if re:
            print(msg)
            global login_info
            login_info = user_name
            break


# check_balance
@common.outer
def check_balance():
    print('Checking your balance ... >>>')
    re_balance = bank_interface.check_balance_interface(login_info)
    print(re_balance)


# withdraw
@common.outer
def withdraw_balance():
    print('Withdraw function is being carried out >>>')
    money = input('Please type the amount you would like to withdraw >>> : ')

    re, msg = bank_interface.withdraw_balance_interface(login_info, money)
    if re:
        print(msg)
    else:
        print(msg)


# Repayment
@common.outer
def repay():
    print('Repayment function is being carried out >>>')
    while True:
        money = input('Please type the amount you would like to charge >>> : ')
        if money.isdigit():
            re, msg = bank_interface.repay_interface(login_info, money)
            if re:
                print(msg)
                break

        print('Please enter the number!')
        continue


# bank_transfer
@common.outer
def transfer():
    print('Transformation function is being carried out >>>')
    target_user = input('Please type the account which you want to transfer >>> : ')
    transfer_money = input('Please type the amount you would like to transfer >>> : ')
    if transfer_money.isdigit():
        re, msg = bank_interface.transfer_interface(login_info, target_user, transfer_money)
        if re:
            print(msg)
        if not re:
            print(msg)


# check the bank statements
@common.outer
def check_flow():
    print('Checking your bank statements...>>>')
    flow_list = bank_interface.check_flow_interface(login_info)
    if flow_list:
        for flow in flow_list:
            print(flow)
    print(f'Account:{login_info} has not generated any statements.')


# Shopping
@common.outer
def shopping():
    shop_list = [
        ['Pork', 30],
        ['Beef', 40],
        ['Ramen', 50],
        ['Sushi', 60],
        ['shirts', 222]
    ]
    shopping_car = {}  # {'item_name':[quantity,price]}
    while True:
        print('=' * 20)
        for index, item in enumerate(shop_list):
            item_name, item_price = item
            print(index)
            print(f'Item name :{item_name}')
            print(f'Item price:{item_price}')
            print('-' * 5)
        print('-' * 20)

        choice1 = input('If you want to buy the item , please enter the number (0~5)>>> : ').strip()

        if not choice1.isdigit():
            print('Please enter the number!')
            continue

        choice1 = int(choice1)

        choice2 = input('Enter <y>:purchase directly or <n>:Put it in your shopping-cart >>> : ').strip()

        if choice2 == 'y':

            flag, msg = shop_interface.shopping_interface(
                login_info, shopping_car
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)

        elif choice2 == 'n':
            item_name, item_price = shop_list[choice1]
            if item_name in shopping_car:
                shopping_car[item_name][1] += 1
            else:
                shopping_car[item_name] = [item_name, 1]
            print('Your shopping-cart:[', shopping_car, ']')

            flag, msg = shop_interface.add_shopcar_interface(
                login_info, shopping_car
            )
            if flag:
                print(msg)
                break


# Check the shopping-cart
@common.outer
def check_shop_car():
    print('Checking your shopping-cart')
    msg = shop_interface.check_shop_car_interface(
        login_info
    )
    print(msg)


Repo = {
    '0': register,
    '1': login,
    '2': check_balance,
    '3': withdraw_balance,
    '4': repay,
    '5': transfer,
    '6': check_flow,
    '7': shopping,
    '8': check_shop_car
}


def run():
    while True:
        print(
            '''
            ==== ATM+Shopping function is being carried out ====
            0:Register
            1:Login-in
            2:check balance
            3:withdraw 
            4:repayment
            5:bank transfer
            6:check bank statement
            7:shopping
            8：check shopping-cart
            '''
        )
        user_choice = input(' >>> : What do you want to do ? (Please enter the number) >>> : ')
        if not user_choice.isdigit():
            print('please enter the number')
            continue

        Repo[user_choice]()
