# Created by Hyun at 3/11/2023
Feature: Create Test Case for functions on Amazon

  Scenario: User can search for a table on Amazon
    Given Open Amazon page
    When Input text table
    When click on search button
    Then verify that text "table" is shown

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign in page is opened

 Scenario: 'Your Amazon Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present

 Scenario: Verify the cart number and add correct product name
    Given Open http://www.amazon.com product page
    When Click add to cart
    And Store the product name
    And Store the count on the cart basket
    Then Click go to cart
    And Verify the cart number 1 added
    And Verify the correct product name displayed