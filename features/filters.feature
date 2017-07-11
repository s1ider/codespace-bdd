Feature: Filters

    Scenario: Filter by price
        Given I am on 'Login' page
        When Navigate to 'Women->Pants & Denim'
        When Filter by 'Price->$100.00 - $199.99'
        When Filter by 'Size->2'
        When Filter by 'Color->Black'
        Then Stop

