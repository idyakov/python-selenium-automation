Feature: Search tests
  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    When Click add to cart
    When Click on Cart icon
    Then Verify search results are shown for <expected_item>
    Examples:
    |item         |expected_item  |
    |tea          |tea            |
    |coffee       |coffee         |

#  Scenario: Verify that user can see product names and images
#    Given Open target main page
#    When Search for iphone 15
#    Then Verify that every product has a name and an image

#    Scenario: User can search for a product
#    Given Open Target main page
#    When Search for tea
#    Then Verify that product has a name and an image
#    When Click add to cart
#    When Click on Cart icon
#    Then Verify search results are shown for tea
