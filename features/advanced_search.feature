Feature: Advanced Search


	Scenario: Hold by beer
		Given I am on 'Login' page
		When Click on link 'Advanced Search'
		When Fill form:
			| label       | value  | type   |  
			| Name        | test   | input  |  
			| Description | desc   | input  |  
			| Color       | Green  | select |  
			| Size        | M      | select |  
			| Gender      | Male   | select |  
			| Gender      | Female | select |  
		When Click on button 'Search'
		Then Fail
