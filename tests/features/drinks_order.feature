Feature: Can place new drinks order
    A customer goes to the café and places a new drinks order

    Scenario: Place new drinks order
        Given a tab opened
        When the drink is ordered
        Then the drink order is placed with Caipirinha costing 5.00 dollars
        and Marguerita costing 10.00 dollars
