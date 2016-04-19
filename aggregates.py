from events import TabOpened
from exc import TabNotOpen


class Aggregate(object):
    pass


class TabAggregate(Aggregate):
    def __init__(self):
        self.opened = False

    def open_tab(self, open_tab):
        return TabOpened(
            open_tab.nid, open_tab.table_number, open_tab.waiter
        )

    def place_order(self, order):
        if not self.opened:
            raise TabNotOpen("Cannot open new tab")
