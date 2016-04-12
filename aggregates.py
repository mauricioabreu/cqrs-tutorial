from events import TabOpened


class Aggregate(object):
    pass


class TabAggregate(Aggregate):

    def open_tab(self, open_tab):
        return TabOpened(
            open_tab.nid, open_tab.table_number, open_tab.waiter
        )
