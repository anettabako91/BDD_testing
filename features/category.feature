Feature: Category filter feature

  Background:
    Given I am on the homepage

  @category
  Scenario Outline: Check category filter
    When I click on "<category>" button
    Then I should see "<subcategory1>", "<subcategory2>" and "<subcategory3>" subcategories
    Examples:
      | category   | subcategory1   | subcategory2 | subcategory3 |
      | Computers  | Desktops       | Notebooks    | Software     |
      | Electronics| Camera & photo |  Cell phones |   Others     |
      | Apparel    | Shoes          | Clothing     |  Accessories |


#daca vrem sa verificam aceleasi scenarii de mai multe ori, asa cu scenario outline e cel mai usor
#atentie mare cum scriem category neaparat "<>"

#  @category
#  Scenario: Check Electronics category
#    When I click on "Electronics" button
#    Then I should see "Camera & photo", "Cell phones" and "Others" subcategories
#
#  @category
#  Scenario: Check Apparel category
#    When I click on "Apparel" button
#    Then I should see "Shoes", "Clothing" and "Accessories" subcategories