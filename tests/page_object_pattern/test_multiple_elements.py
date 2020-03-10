from src.page_object_pattern.multiple_elements import MultipleElements
from src.page_object_pattern.test_template import TestTemplate
import unittest

class TestMultipleElements(TestTemplate):

    def test_multiple_select(self):
        """
        To confirm
        """
        main_page = MultipleElements(self.driver)
        assert main_page.multiple_select_all
        assert (main_page.multiple_select_by_index(1))
        assert main_page.multiple_select_by_value('apple')
        assert main_page.multiple_select_by_text('Peach')

if __name__ == '__main__':
    unittest.main()