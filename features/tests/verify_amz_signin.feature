# Created by Hyun at 2/15/2023
Feature: verify sign in amazon.com
  # Enter feature description here

  Scenario: amazon sign in clicking on return and order
    Given Open https://www.amazon.com
    When Click Orders
    Then Sign In header is visible
    And email input field is present