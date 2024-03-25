Feature: Login Feature

  Background:
    Given I am on the login page

  @first
  Scenario: Login with wrong credentials
    When I enter "mail@email.com" in email field
    And I enter "password123" in password field
    And I press the login button
    Then I should see an error message

  @second
  Scenario: Enter wrong email format
    When I enter "mail.com" in email field
    And I press the login button
    Then I should see an error for email