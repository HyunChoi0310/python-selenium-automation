# Created by Hyun at 2/15/2023
Feature: Test scenario of amazon cart is empty
  # Enter feature description here

  Scenario: verify amazon cart is empty
    Given Open https://www.amazon.com
    When Click the cart
    Then Your Amazon Cart is empty is visible