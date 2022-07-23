# Created by thoma at 7/23/2022
Feature: Amazon Cart Tests
  # Enter feature description here

  Scenario: User can click for cart 0
    Given Open Amazon page1
    When Click for cart 0 on amazon
    Then User verify cart for empty