# Created by Hyun at 3/1/2023
Feature: Test Case for loop
  Make a test case with a loop. You can use color selection for any product page you like.
  Create 1 test case that will loop through colors: it should click on each color and verify
  that color has been selected.
  Product example with multiple colors:
  https://www.amazon.com/gp/product/B07BJKRR25/

  Scenario Outline: Create Test Case with loop through colors
    Given Open Amazon product <product> page
    Then Verify that color has been selected by clicking
    Examples:
      | product |
      | B096VQ1BQX |
#      | B07TW8MN4R |
# tried several products, how to set the expected colors?


  Scenario: Test Case that search page has product name and image
    Given Open Amazon page
    When Search coffee maker product
    Then Verify correct product name and image
# HW5_3 : Approach idea: Inside result, the number of product name and image will be same -> len(name)=len(image)
# but the number is different, not correct css_selector? or not right approach?
