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
        msg = f'用户:[{login_user}]支付成功,扣款{cost}$,准备发货...'
        shop_logger.info(msg)
        return True, msg

    return False, '支付失败,金额不足或其他原因,请检查.'


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
    return True, '添加购物车成功'


def check_shop_car_interface(login_user):
    re = db_handler.select(login_user)
    re_shopcar = re.get('shop_car')
    return re_shopcar
