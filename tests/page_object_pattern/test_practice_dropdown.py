"""
Description: Test module for module src/page_object_patter/base_page.py

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.dropdown_section import Dropdown
from src.page_object_pattern.test_template import TestTemplate
import time
import unittest


class TestHomePage(TestTemplate):
    """
    Check page functionality
    """
    def test_select_option_index(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_index(1)
        time.sleep(4)

    def test_select_option_value(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_value("honda")
        time.sleep(4)

    def test_select_visible_text(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_visible_text("Honda")
        time.sleep(4)


    


if __name__ == '__main__':
    unittest.main()
