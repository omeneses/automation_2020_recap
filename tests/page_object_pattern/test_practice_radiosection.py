"""
Description: Test module for module src/page_object_patter/base_page.py

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.radio_section import Practice
from src.page_object_pattern.test_template import TestTemplate
import unittest


class TestHomePage(TestTemplate):
    """
    Check page functionality
    """
    def test_verify_title(self):
        main_page = Practice(self.driver)
        print(main_page.get_title_text())


    


if __name__ == '__main__':
    unittest.main()
