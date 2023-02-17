# Created by Hyun at 2/16/2023
Feature: Test scenario of add products into the cart
  # E

  Scenario: Verify the cart number on adding the products
    Given Open http://www.amazon.com product page
    When Click add to cart
    Then The number on the cart is added