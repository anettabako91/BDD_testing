from behave import *


@given('I am on the homepage')
def step_impl(context):
    context.CategoryPage.navigate_to_homepage()


@when('I click on "{category}" button')
def step_impl(context,category):
    context.CategoryPage.click_on_category_button(category)


@then('I should see "{category1}", "{category2}" and "{category3}" subcategories')
def step_impl(context, category1, category2, category3):
    subcategories_elements = context.CategoryPage.get_subcategories()
    actual_categories = []
    for element in subcategories_elements:
        actual_categories.append(element.text)

    assert len(actual_categories) == 3
    assert category1 in actual_categories,f'{category1} is not in {actual_categories}'
    assert category2 in actual_categories,f'{category2} is not in {actual_categories}'
    assert category3 in actual_categories,f'{category3} is not in {actual_categories}'
