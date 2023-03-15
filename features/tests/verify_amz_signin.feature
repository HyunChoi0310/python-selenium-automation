# Created by Hyun at 2/15/2023
Feature: verify sign in amazon.com
  # Enter feature description here

#  Scenario: amazon sign in clicking on return and order
#    Given Open https://www.amazon.com
#    When Click Orders
#    Then Sign In header is visible
#    And email input field is present

# Scenario: Sign in page can be opened from Sign in
#    Given Open Amazon page
#    When Click Sign in from popup
#    Then Verify Sin in page

  Scenario: Sign in page can be opened from sign in popup
      Given Open Amazon page
      Then Verify Sign in popup shown
      When Wait for 8 sec
      Then Verify Sign in popup disappears

