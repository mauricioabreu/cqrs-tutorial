Feature: Can open a new tab
    A customer goes to the café and makes its drink or food request

    Scenario: Open new tab
        When the customer makes its request at table 42
        Then a new tab of id 1 is openend by Derek at table 42
