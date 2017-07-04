Feature: Registration

	Scenario: Almost successfull registration
		Given I am on 'Registration' page
		When Fill text form:
			| label            | value          |  
			| First Name       | Robot          |  
			| Last Name        | Bobot          |  
			| Email Address    | r2d2@gmail.com |  
			| Password         | 1234           |  
			| Confirm Password | 1234           |  
		When Click on button 'Register'
		When Click on checkbox 'Sign Up for Newsletter'
		Then Header 'Create an Account' should be displayed
		Then Fail