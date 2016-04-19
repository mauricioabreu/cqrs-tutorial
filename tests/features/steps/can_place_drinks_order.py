from behave import given, then, when

from aggregates import TabAggregate
from commands import OpenTab, PlaceOrder
from events import DrinksOrdered, OrderedItem


@given('a tab opened')
def tab_opened(context):
    tab = TabAggregate()
    tab.open_tab(
        OpenTab(1, 42, "Derek")
    )
    context.tab = tab


@when('the drink is ordered')
def drink_is_ordered(context):
    order = PlaceOrder(
        1,
        [DrinksOrdered(1, [OrderedItem(1, "Caipirinha", True, 5.00)])]
    )
    context.tab.place_order(order)


@then('the drink order is placed with Caipirinha costing 5.00 dollars')
def caipirinha_is_placed(context):
    pass


@then('Marguerita costing 10.00 dollars')
def marguerita_is_placed(context):
    pass
