class TabOpened(object):

    def __init__(self, nid, table_number, waiter):
        self.nid = nid
        self.table_number = table_number
        self.waiter = waiter


class OrderedItem(object):

    def __init__(self, menu_number, description, is_drink, price):
        self.menu_number = menu_number
        self.description = description
        self.is_drink = is_drink
        self.price = price


class DrinksOrdered(object):

    def __init__(self, nid, items):
        self.nid = nid
        self.items = items


class FoodOrdered(object):

    def __init__(self, nid, items):
        self.nid = nid
        self.items = items
