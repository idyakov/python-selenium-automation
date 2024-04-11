Feature: Test Scenarios for Search Target pages functionality

  Scenario: Developer checking the expected words on the Target pages
    Given Open Target main page
    When Target cart button pressed
    Then Verify the cart is empty shown

  Scenario: Developer checking the expected SignIn functionality on the Target pages
    Given Open Target main page
    When Target Signin button pressed
    Then Verify Sign In form opened

