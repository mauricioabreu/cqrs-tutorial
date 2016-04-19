from behave import then, when

from aggregates import TabAggregate
from commands import PlaceOrder
from events import DrinksOrdered, OrderedItem
from exc import TabNotOpen


@when('the place is ordered')
def place_is_ordered(context):
    tab = TabAggregate()
    order = PlaceOrder(
        1,
        [DrinksOrdered(1, [OrderedItem(1, "Caipirinha", True, 5.00)])]
    )
    try:
        tab.place_order(order)
    except TabNotOpen:
        context.status = "failed"


@then('the order is not placed because the tab was not opened')
def tab_was_not_opened(context):
    assert context.status == "failed"
