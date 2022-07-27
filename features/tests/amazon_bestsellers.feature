# Created by thoma at 7/24/2022
Feature: Verify 5 Best Sellers on Amazon
  # Enter feature description here

  Scenario: User can see 5 best sellers on amazon
    Given Open Amazon best sellers page
    Then User sees 5 best sellers links