Feature: Cart

    Background:
        Given Logged in with default credentials
        Given I am on 'Cart' page

	Scenario: Verify grand total on checkout
        When Change qty of product #1 to 1
		When Change qty of product #2 to 2
		Then Verify grand total equals to sum of all prices

    # @wip
    # Scenario Outline: Validate qty of products
    #     When Change qty of product #1 to <qty>
    #     Then Text 'Invalid qty' should be displayed

    # Examples:
    #     | qty |
    #     | 0   |
    #     | -1  |
    #     | 999 |
        