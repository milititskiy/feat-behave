Feature: Sample Login Test
  As a user
  I want to test the login functionality
  So that I can verify the authentication works correctly

  @smoke
  Scenario: Successful login
    Given I am on the login page
    When I enter username "testuser"
    And I enter password "password123"
    And I click the login button
    Then I should be logged in successfully

  @regression
  Scenario: Invalid login
    Given I am on the login page
    When I enter username "invalid"
    And I enter password "wrong"
    And I click the login button
    Then I should see an error message
