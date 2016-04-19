class OpenTab(object):

    def __init__(self, nid, table_number, waiter):
        self.nid = nid
        self.table_number = table_number
        self.waiter = waiter


class PlaceOrder(object):

    def __init__(self, nid, items):
        self.nid = nid
        self.items = items
