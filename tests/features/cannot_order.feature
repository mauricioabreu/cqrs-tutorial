Feature: Cannot place new order
    A customer goes to the café and places a new order

    Scenario: Place new order
        When the place is ordered
        Then the order is not placed because the tab was not opened 
