Feature: Registration

    Background: 
        Given I am on 'Registration' page

	Scenario: Almost successfull registration
		When Fill form:
			| label                  | value          | type     |  
			| First Name             | Robot          | input    |  
			| Last Name              | Bobot          | input    |  
			| Email Address          | r2d2@gmail.com | input    |  
			| Password               | 1234           | input    |  
			| Confirm Password       | 1234           | input    |  
			| Sign Up for Newsletter | x              | checkbox |  
		When Click on button 'Register'
		Then Header 'Create an Account' should be displayed

    @w
    Scenario: Successfull registration
        When Fill text form:
            | label                  | value          |
            | First Name             | Robot          |
            | Last Name              | Bobot          |
            | Email Address          | <random_email> |
            | Password               | superstrong!1  |
            | Confirm Password       | superstrong!1  |
        When Click on button 'Register'
        Then Text 'Thank you for registering with Madison Island.' should be displayed