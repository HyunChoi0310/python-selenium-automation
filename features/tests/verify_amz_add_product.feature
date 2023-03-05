# Created by Hyun at 2/16/2023
Feature: Test scenario of add products into the cart
  # E

 # Scenario: Verify the cart number on adding the products
 #   Given Open http://www.amazon.com product page
 #   When Click add to cart
 #   Then The number on the cart is added

  Scenario: Verify the cart number and add correct product name
    Given Open http://www.amazon.com product page
    When Click add to cart
    And Store the product name
    And Store the count on the cart basket
    Then Click go to cart
    And Verify the correct product name displayed
    Then Verify the cart number 1 added