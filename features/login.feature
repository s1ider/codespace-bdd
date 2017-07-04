Feature: Login

	Scenario: Demo Login
		Given I am on 'Login' page
		When Fill text form:
			| label         | value                 |  
			| Email Address | s1iderorama@gmail.com |  
			| Password      | codespace             |  
		When Click on button 'Login'
		Then Header 'My Dashboard' should be displayed
		
