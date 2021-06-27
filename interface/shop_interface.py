from lib import common
from db import db_handler

shop_logger = common.get_logger(log_type='shop')


def shopping_interface(login_user, shop_car):
    cost = 0
    items = shop_car.values()
    for price, quantity in items:
        total_price = price * quantity
        cost += total_price
    from interface import bank_interface
    flag = bank_interface.pay_interface(
        login_user, cost
    )
    if flag:
        msg = f'Account:[{login_user}] purchasing successfully,deduction:{cost}$'
        shop_logger.info(msg)
        return True, msg

    return False, 'Error, check your account balance or contact to our operator!'


def add_shopcar_interface(login_user, shopping_car):
    user_dict = db_handler.select(login_user)
    for item_name, price_quantity in shopping_car.items():
        quantity = price_quantity[1]

        if item_name in user_dict.get('shop_car'):
            user_dict['shop_car']['item_name'][1] += quantity

        else:
            user_dict['shop_car'].update(
                {item_name: price_quantity}
            )

        db_handler.save(login_user, user_dict)
    return True, 'Add to cart successfully!'


def check_shop_car_interface(login_user):
    re = db_handler.select(login_user)
    re_shopcar = re.get('shop_car')
    return re_shopcar
