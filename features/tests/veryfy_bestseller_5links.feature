# Created by Hyun at 2/21/2023
Feature: Test Case for bestseller links on Amazon

  Scenario: Best seller links are 5
    Given Open Amazon bestseller page
    Then Verify 5 links on the header
    And Verify correct page open, close and back to page


# Scenario: Customer Service page is visible
#    Given Open Amazon bestseller page
#    When Click Amazon Customer Service page
#    Then Verify Customer Service is visible
#    And Verify Customer Service 10 links
#    And Verify Customer Service Help is visible
#    And Verify Customer Service Input_Field is present
#    And Verify Customer Service Help Topic is visible

