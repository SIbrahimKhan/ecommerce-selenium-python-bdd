@cart
Feature: Cart and Checkout
  add priducts to cart and complete the checkout flow

  Background:
    Given the user is on login page
    Given the user logs in as "standard_user"
    Then the user land on product page

  @smoke
  Scenario: Add a single product to cart
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge should show "1" item
  
  @regression
  Scenario: Add multiple product to cart
    When the user adds the following products to cart:
      | product_name |
      | Sauce Labs Backpack |
      | Sauce Labs Bike Light | 
      | Sauce Labs Bolt T-Shirt |
    Then the cart badge should show "3" item
  
  @regression
  Scenario: Remove product from cart
    Given the user has added "Sauce Labs Backpack" to cart
    When the user opens the cart
    And removes the first item from the cart
    Then the cart should be empty

  @smoke @e2e
  Scenario: Complete end to end checkout flow
    Given the user has added "Sauce Labs Bike Light" to cart
    When the user opens the cart
    And proceeds to checkout
    And fills the checkout info "test" "user" "388891"
    And finish the checkout
    Then the user should see the order confirmation message "Thank you for your order!"

  @regression @negative
  Scenario: Checkout fails when the required info is missing
    Given the user has added "Sauce Labs Bolt T-Shirt" to cart
    When the user opens the cart
    And proceeds to checkout
    And fills the checkout info "" "user" "560001"
    Then the user should see the checkout error message