# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box import VendingMachine, divide, get_grade, is_even, is_triangle, check_number_status, validate_password, calculate_total_discount, calculate_order_total, calculate_items_shipping_cost, validate_login, verify_age, categorize_product
from white_box import TrafficLight, UserAuthentication, ShoppingCart, Product

class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

###My Tests

class TestWhiteBox2(unittest.TestCase):
    def test_check_number_status_positive(self):

        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password_success(self):
        self.assertTrue(validate_password("Test!password123"))

    def test_validate_password_length_error(self):
        self.assertFalse(validate_password("Sh0rt!"))

    def test_validate_password_no_uppercase(self):
        self.assertFalse(validate_password("test!password123"))

    def test_validate_password_no_lowercase(self):
        self.assertFalse(validate_password("TEST!PASSWORD123"))

    def test_validate_password_no_digit(self):
        self.assertFalse(validate_password("Test!password"))

    def test_validate_password_no_specialchar(self):
        self.assertFalse(validate_password("Testpassword123"))

    def test_calculate_total_discount_zero(self):
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_10(self):
        self.assertEqual(calculate_total_discount(250), 25)

    def test_calculate_total_discount_20(self):
        self.assertEqual(calculate_total_discount(750), 150)

    def test_calculate_order_total_0(self):
        self.assertEqual(calculate_order_total([{"name":"keyboard", "quantity" : 1, "price": 100}]), 100)

    def test_calculate_order_total_95(self):
        self.assertEqual(calculate_order_total([{"name":"keyboard", "quantity" : 8, "price": 100}]), 760)

    def test_calculate_order_total_90(self):
        self.assertEqual(calculate_order_total([{"name":"keyboard", "quantity" : 15, "price": 100}]), 1350)

    def test_calculate_items_shipping_cost_standard_10(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 3}], "standard"), 10)

    def test_calculate_items_shipping_cost_standard_15(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 7}], "standard"), 15)

    def test_calculate_items_shipping_cost_standard_20(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 15}], "standard"), 20)

    def test_calculate_items_shipping_cost_express_20(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 3}], "express"), 20)

    def test_calculate_items_shipping_cost_express_30(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 7}], "express"), 30)

    def test_calculate_items_shipping_cost_express_40(self):

        self.assertEqual(calculate_items_shipping_cost([{"name": "book", "weight" : 15}], "express"), 40)

    def test_calculate_items_shipping_cost_invalid_shipping_method(self):

        self.assertRaises(ValueError,calculate_items_shipping_cost, [{"name": "book", "weight" : 3}], "normal")

    def test_validate_login_success(self):

        self.assertEqual(validate_login("testuser", "testpassword"), "Login Successful")

    def test_validate_login_fail_username(self):

        self.assertEqual(validate_login("test", "testpassword"), "Login Failed")

    def test_validate_login_fail_password(self):

        self.assertEqual(validate_login("testuser", "test"), "Login Failed")

    def test_verify_age_eligible(self):

        self.assertEqual(verify_age(20), "Eligible")

    def test_verify_age_not_eligible(self):

        self.assertEqual(verify_age(10), "Not Eligible")

    def test_categorize_product_A(self):

        self.assertEqual(categorize_product(25), "Category A")

    def test_categorize_product_B(self):

        self.assertEqual(categorize_product(75), "Category B")

    def test_categorize_product_C(self):

        self.assertEqual(categorize_product(125), "Category C")

    def test_categorize_product_D(self):

        self.assertEqual(categorize_product(225), "Category D")

class TestTrafficLight(unittest.TestCase):

    def setUp(self):
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_traffic_light_change_green_success(self):

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Green")

    def test_traffic_light_change_yellow_success(self):

        self.traffic_light.state = "Green"

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Yellow")

    def test_traffic_light_change_red_success(self):

        self.traffic_light.state = "Yellow"

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Red")

    def test_traffic_light_get_current_state_success(self):

        output = self.traffic_light.get_current_state()

        self.assertEqual(output, "Red")

class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.user_authentication = UserAuthentication()
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_loggin_state(self):
        output = self.user_authentication.login()

        self.assertEqual(self.user_authentication.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_login_success_no_success(self):
        self.user_authentication.state = "Logged In"

        output = self.user_authentication.login()
        self.assertEqual(output, "Invalid operation in current state")

    def test_logout_success(self):
        self.user_authentication.state = "Logged In"
        output = self.user_authentication.logout()
        self.assertEqual(output, "Logout successful")

    def test_logout_no_success(self):
        self.user_authentication.state = "Logged Out"
        output = self.user_authentication.logout()
        self.assertEqual(output, "Invalid operation in current state")

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.assertEqual(self.shopping_cart.items, [])

    def test_add_product(self):
        self.shopping_cart.add_product("keyboard")
        self.assertEqual(self.shopping_cart.items, [{"product": "keyboard", "quantity": 1}])

    def test_add_multiple_products(self):
        self.shopping_cart.add_product("keyboard")
        self.shopping_cart.add_product("keyboard")
        self.assertEqual(self.shopping_cart.items, [{"product": "keyboard", "quantity": 2}])

    def test_remove_product(self):

        self.shopping_cart.add_product("keyboard",2)
        self.shopping_cart.remove_product("keyboard")
        self.assertEqual(self.shopping_cart.items, [{"product": "keyboard", "quantity": 1}])

    def test_view_cart(self):

        product1 = Product("keyboard",100)
        self.shopping_cart.add_product(product1)
        output = self.shopping_cart.view_cart()
        self.assertEqual(output, "1 x keyboard - $100")

    def test_checkout(self):
        product1 = Product("keyboard",100)
        self.shopping_cart.add_product(product1)
        output = self.shopping_cart.checkout()
        self.assertEqual(output, "Total: $100\n Checkout completed. Thank you for shopping!")
