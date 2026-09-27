Feature: User Login

 Background:
    Given the user is on login page
 
 @smoke
 Scenario: Successful login wiht valid creds
    When the user logs in as "standard_user"
    Then the user land on product page
    
 @regression
 Scenario: Login failed for locked out user
    When the user logs in as "locked_out_user"
    Then the user should see the error message "Sorry, this user has been locked out."
 @regression
 Scenario Outline: User login with invalid creds
    When the user logs in with invalid creds "<username>" and password "<password>"
    Then the user should see the error message

    Examples:
      | username      | password      |
      | invalid_user  | secret_sauce  |
      | standard_user | wrong_password|
      |               | secret_sauce  |
      | standard_user |               |