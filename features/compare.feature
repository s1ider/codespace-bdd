Feature: Compare products

    Scenario: Compare two product
        Given I am on 'Login' page
        When Navigate to 'Women->Pants & Denim'
        When Select product #1 for compare
        When Select product #2 for compare
        When Click on button 'Compare'
        Then 'Products Comparison List' popup should be displayed
        When Close popup
