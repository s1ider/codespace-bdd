Feature: Filters

    
    Scenario: Filter by price
        Given I am on 'Login' page
        When Navigate to 'Women->Pants & Denim'
        When Filter by 'Price->$100.00 - $199.99'
        When Filter by 'Size->2'
        When Filter by 'Color->Black'
        Then Stop

    @smoke
    Scenario: Apply filter
        Given I am on 'Login' page
        When Navigate to 'Accessories->Shoes'
        When Store number of products
        When Filter by 'Price->$200.00 - $299.99'
        Then Number of products should be less then stored value

