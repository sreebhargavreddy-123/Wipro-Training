import uuid
import pytest
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from utilities.config_reader import ConfigReader
from utilities.csv_reader import read_csv_data
from utilities.messages import Messages


test_data = read_csv_data(ConfigReader.get_test_data_path())


@pytest.mark.parametrize(
    "user_data",
    test_data,
    ids=[f"{d['first_name']}_{d['search_product']}" for d in test_data]
)
def test_complete_user_journey(setup, user_data, logger):

    driver = setup
    logger.info("===== Starting Complete User Journey Test =====")

    # STEP 1: REGISTER
    logger.info("Clicking Register")
    home = HomePage(driver)
    home.click_register()

    register_page = RegisterPage(driver)

    email = f"user_{uuid.uuid4()}@test.com"
    logger.info(f"Generated email: {email}")

    logger.info("Registering new user")
    register_page.register_user(
        user_data["first_name"],
        user_data["last_name"],
        email,
        user_data["password"],
        user_data["gender"]
    )

    assert Messages.REGISTRATION_SUCCESS in register_page.get_success_message()
    logger.info("Registration successful")

    # STEP 2: LOGOUT
    logger.info("Logging out after registration")
    home.click_logout()

    # STEP 3: LOGIN
    logger.info("Clicking Login")
    home.click_login()

    login_page = LoginPage(driver)
    logger.info("Logging in with registered credentials")
    login_page.login(email, user_data["password"])

    assert login_page.is_login_successful()
    logger.info("Login successful")

    # STEP 4: SEARCH PRODUCT
    logger.info(f"Searching product: {user_data['search_product']}")
    search_page = SearchPage(driver)
    search_page.search_product(user_data["search_product"])

    assert search_page.has_results()
    logger.info("Search results displayed")

    # STEP 5: PRODUCT DETAILS
    logger.info("Opening first product from results")
    search_page.open_first_product()

    product_page = ProductPage(driver)

    assert product_page.get_product_title()
    assert product_page.get_product_price()
    logger.info("Product title and price verified")

    # STEP 6: ADD TO CART
    logger.info("Adding product to cart")
    product_page.add_to_cart()

    assert Messages.ADD_TO_CART_SUCCESS in product_page.get_success_notification()
    logger.info("Product added to cart successfully")

    # STEP 7: UPDATE CART
    logger.info("Navigating to cart")
    home.click_cart()

    cart_page = CartPage(driver)

    logger.info(f"Updating cart quantity to {user_data['quantity']}")
    cart_page.update_quantity(int(user_data["quantity"]))

    assert cart_page.is_quantity_updated(int(user_data["quantity"]))
    logger.info("Cart quantity updated successfully")

    # STEP 8: REMOVE ITEM
    logger.info("Removing item from cart")
    cart_page.remove_item()

    assert cart_page.is_cart_empty(Messages.EMPTY_CART)
    logger.info("Cart is empty after removal")

    # STEP 9: LOGOUT
    logger.info("Logging out")
    home.click_logout()

    # STEP 10: SESSION VALIDATION
    logger.info("Validating session by accessing customer info page")
    driver.get(
        ConfigReader.get_base_url() +
        ConfigReader.get_customer_info_url()
    )

    assert Messages.LOGIN_PAGE_TITLE in driver.title
    logger.info("Session validation successful")

    logger.info("===== Test Completed Successfully =====")
