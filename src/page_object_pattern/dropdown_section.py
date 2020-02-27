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
    Home page
    """
    DROPDOWN_TEXT = '//*[@id="select-class-example"]/fieldset/legend'
    DROPDOWN_OPTION = 'carselect'

    

    def get_title_text(self):
        return self._driver.find_element_by_xpath(Dropdown.DROPDOWN_TEXT).text
        
    def select_index(self, index):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_OPTION))
        s1.select_by_index(index)

    def select_value(self, value):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_OPTION))
        s1.select_by_value(value)

    def select_visible_text(self, showtext):
        s1 = Select(self._driver.find_element_by_id(Dropdown.DROPDOWN_OPTION))
        s1.select_by_visible_text(showtext)
