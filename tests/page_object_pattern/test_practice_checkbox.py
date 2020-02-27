"""
Description: Test module for module src/page_object_patter/base_page.py
@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.checkbox_section import Checkbox
from src.page_object_pattern.test_template import TestTemplate
import time
import unittest


class TestHomePage(TestTemplate):
    """
    Check page functionality
    """
    def test_check_option_bmw(self):
        checkbox = Checkbox(self.driver)
        print(checkbox.get_title_text())
        checkbox.check_element(checkbox.CHECKBOX_BENZ)
        time.sleep(4)

    def test_check_option_benz(self):
        checkbox = Checkbox(self.driver)
        print(checkbox.get_title_text())
        checkbox.check_benz()
        time.sleep(4)

    def test_check_option_honda(self):
        checkbox = Checkbox(self.driver)
        print(checkbox.get_title_text())
        checkbox.check_honda()
        time.sleep(4)


    


if __name__ == '__main__':
    unittest.main()