# Created by Hyun at 3/8/2023
Feature: Test for 404 page on Amazon


  Scenario: User is able to navigate to amazon blog from
    Given Open Amazon product B0B8M5FBFQ11111 page
    And Store original window
    When Click on a dog image
    And Switch to the new window
    Then verify blog is opened
    And Close blog
    And Return to original window