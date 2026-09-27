@sort
Feature: Product Sorting
    Sorting the products by price and name

    Background:
     Given the user is on login page
     Given the user logs in as "standard_user"
     Then the user land on product page
    
    @regression
    Scenario: Sort product by price low to high
     When the user sort product by "Price (low to high)"
     Then the products should be listed in ascending price order

    @regression
    Scenario: Sort product by price high to low
     When the user sort product by "Price (high to low)"
     Then the products should be listed in descending price order

    Scenario: Sort product by name a to z
     When the user sort product by "Name (A to Z)"
     Then the products should be listed as a to z

    Scenario: Sort product by name z to a
     When the user sort product by "Name (Z to A)"
     Then the products should be listed as z to a