from behave import then, when

from aggregates import TabAggregate
from commands import OpenTab


@when('the customer makes its request at table 42')
def when_open_tab(context):
    tab = TabAggregate()
    context.tab_opened = tab.open_tab(
        OpenTab(1, 42, "Derek")
    )


@then('a new tab of id 1 is openend by Derek at table 42')
def tab_is_opened(context):
    assert context.tab_opened.nid == 1
    assert context.tab_opened.table_number == 42
    assert context.tab_opened.waiter == "Derek"
