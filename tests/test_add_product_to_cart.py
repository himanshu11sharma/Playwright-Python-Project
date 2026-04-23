"""
Test Case: Add Product to Cart

===========================================
Manual Test Steps
===========================================

1. Open the application in the browser.
2. Locate the search box on the homepage.
3. Enter a valid product name (e.g., "iPhone") and click the Search button.
4. Verify that the search results page displays products matching the entered name.
5. Select the desired product from the list.
6. On the product page, update the product quantity (e.g., 2).
7. Click on the "Add to Cart" button.
8. Verify that a success confirmation message is displayed indicating
   the product has been successfully added to the cart.

Expected Result:
----------------
The product should be successfully added to the shopping cart,
and a visible confirmation message should appear.
"""

import pytest
from playwright.sync_api import expect,Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config

@pytest.mark.regression
def test_add_product_to_cart(page:Page):
    """
        Automated Test Case: Verify user can search and add a product to the cart.
        """

    # --- Test Data ---

    product_name=Config.product_name    # get product name from configuration file
    quantity=Config.product_quantity    # get product quantity from configuration file

    # --- Page Object Initialization ---

    home_page=HomePage(page)
    search_results_page=SearchResultsPage(page)

    #  ---Step-1 : Search for a product ----
    home_page.enter_product_name(product_name)
    home_page.click_search()

    # ---Step-2: Select the product from search Results ----

    product_page=search_results_page.select_product(product_name)

    # --- Step -3 : set Quantity and add to Cart ----
    product_page.set_quantity(quantity)
    product_page.add_to_cart()

    #  --- Step 4: Verify Confirmation Message ----
    # Ensure the success message appears within 3 seconds after adding the product
    expect(product_page.get_confirmation_message()).to_be_visible(timeout=4000)
