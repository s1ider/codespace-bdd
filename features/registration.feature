Feature: Registration

	Scenario: Almost successfull registration
		Given I am on 'Registration' page
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
		Then Fail