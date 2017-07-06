Feature: Address Book

    Background:
        Given Logged in with default credentials
        Given I am on 'AddressBook' page

    Scenario: Add new address
        When Try click on button 'Add New Address'
        When Fill checkout form with default values
        When Fill form:
            | label                             | value         | type     |  
            | First Name                        | Robot         | input    |  
            | Last Name                         | Bobot         | input    |  
            | Company                           | Robotics Inc  | input    |  
            | Telephone                         | 123123123     | input    |  
            | Fax                               | 123123412     | input    |  
            | Street Address                    | Robo circle 1 | input    |  
            | City                              | Kiev          | input    |  
            | Zip                               | 12345         | input    |  
            | Country                           | Ukraine       | select   |  
            | Use as my default billing address | x             | checkbox |  
        When Click on button 'Save Address'
        Then Text 'The address has been saved.' should be displayed

    Scenario Outline: Edit <address>
        When Click on link '<address>'
        When Fill text form:
            | label      | value     |  
            | First Name | Robobobot |  
        When Click on button 'Save Address'
        Then Text 'The address has been saved.' should be displayed
        
    Examples:
        | address                 |  
        | Change Billing Address  |  
        | Change Shipping Address |  
