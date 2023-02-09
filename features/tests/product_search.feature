# Created by Hyun at 2/09/23
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Peddleboards into search field
    And Click on search icon
    Then Product results for Peddleboards are shown
