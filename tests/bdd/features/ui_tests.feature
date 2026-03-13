Feature: Juice Shop Core UI Functionality
  As a regular customer
  I want to use the main web interface
  So that I can search for products and manage my account

  # Предусловия для каждого сценария
  Background:
    Given I open the Juice Shop home page
    And I dismiss all welcome banners

  @bdd
  Scenario: User can search for a product
    When I search for the product "Apple"
    Then the first result should contain "Apple"

  @bdd
  Scenario: User can view product details
    When I click on the first product on the board
    Then the product dialog title should match the product name

  @bdd
  Scenario: User cannot login with invalid credentials
    When I navigate to the login page
    And I try to login with email "fake_user@test.com" and password "wrong123"
    Then I should see an error message "Invalid email or password."

  @bdd
  Scenario: User can see the site logo
    Then the site logo should be visible