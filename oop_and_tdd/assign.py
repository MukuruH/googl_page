import random


class Order:
    def __init__(self, product_name, deadline):
        self.product_name = product_name
        self.product_id = random.randint(0, 100)
        self.deadline = deadlineimport unittest



class QuickOrder(Order):
    def __init__(self, product_name, deadline, extra_dime):
        super().__init__(product_name, deadline)
        self.delivery_type = 'QuickOrder'
        self.extra_dime = extra_dime

    def check_delivery_type(self):
        return self.delivery_type

    def change_extra_dime(self, extra_dime):
        self.extra_dime = extra_dime


class StandardOrder(Order):
    def __init__(self, product_name, deadline):
        super().__init__(product_name, deadline)
        self.delivery_type = 'StandardOrder'

    def check_delivery_type(self):
        return self.delivery_type


delivered = []


def create_quick_order(product_name, deadline, extra_dime=None):
    if extra_dime < 20000:
        raise ValueError('Extra dime is less than 20000')
    if deadline > 24:
        raise ValueError('Quick order is delivered in less than 24 hrs')
    order = QuickOrder(product_name, deadline, extra_dime)
    delivered.append(order)


def create_standard_order(product_name, deadline):
    order = StandardOrder(product_name, deadline)
    delivered.append(order)

create_standard_order('Watch', 47)
print(delivered)