# Created by Hyun at 3/7/2023
Feature: window handling test case from the class
  and verify that user can open amazon applications
  from Terms of Conditions

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon TC page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original