# Created by thoma at 7/15/2022
Feature: Amazon Product Search Tests
  # Enter feature description here

  Scenario: User can search for mug
    Given Open Amazon page
    When Search for mug on amazon
    Then User sees results for "mug"

  Scenario: User can search for coffee
    Given Open Amazon page
    When Search for coffee on amazon
    Then User sees results for "coffee"