Feature: Target items verification - image <> item
#Scenario_1
 Scenario: Verify that user can see product names and images
    Given Open target main page_
    When Search for_ AirPods (3rd Generation)
    Then Verify that every product has a name and an image


