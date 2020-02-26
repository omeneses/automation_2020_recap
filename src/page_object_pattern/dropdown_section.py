"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage
from selenium.webdriver.support.select import Select



class Dropdown(BasePage):
    """
    Dropdown section
    """
    DROPDOWN_SECTION_TEXT = '//*[@id="select-class-example"]/fieldset/legend'
    DROPDOWN_ID = 'carselect'


    def get_title_text(self):
        return self._driver.find_element_by_xpath(Dropdown.DROPDOWN_SECTION_TEXT).text

    def select_index(self, index):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_ID))
        s1.select_by_index(index)

    def select_value(self, value):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_ID))
        s1.select_by_value(value)

    def select_visible_text(self, visibleText):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_ID))
        s1.select_by_visible_text(visibleText)
