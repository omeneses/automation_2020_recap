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
    """
    User can select the BMW option using the Index of Dropdown.
    """
    def test_select_index(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_index(0)
        time.sleep(5)
    """    
    User can select the BENZ option using the Value of Dropdown
    """
    def test_select_value(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_value("benz")
        time.sleep(5)
    """
    User can select the HONDA option any option using the Text of Dropdown
    """
    def test_select_visible_text(self):
        dropdown = Dropdown(self.driver)
        print(dropdown.get_title_text())
        dropdown.select_visible_text("Honda")
        time.sleep(5)
    

if __name__ == '__main__':
    unittest.main()
