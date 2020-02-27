"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.
@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage

class Checkbox(BasePage):
    """
    Checkbox section
    """
    CHECKBOX_SECTION_TEXT = 'checkbox-example'
    CHECKBOX_BMW = 'bmwcheck'
    CHECKBOX_BENZ = 'benzcheck'
    CHECKBOX_HONDA = 'hondacheck'

    def get_title_text(self):
        return self._driver.find_element_by_id(Checkbox.CHECKBOX_SECTION_TEXT).text

    def check_element(self, element):
        checkboxElement = self._driver.find_element_by_id(element)
        checkboxElement.click()

    def check_bmw(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BMW)
        checkboxElement.click()

    def check_benz(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BENZ)
        checkboxElement.click()

    def check_honda(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_HONDA)
        checkboxElement.click()