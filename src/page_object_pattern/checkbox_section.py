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
        result = checkboxElement.is_selected()
        if result:
            print('Checkbox already selected')
        else:
            checkboxElement.click()
            print('Checkbox selected')

    def element_ischecked(self, element):
        checkboxElement = self._driver.find_element_by_id(element)
        result = checkboxElement.is_selected()
        if result:
            print('Element is already selected')
        else:
            print('Element is not selected')

    # Check each element

    def check_bmw(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BMW)
        checkboxElement.click()

    def check_benz(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BENZ)
        checkboxElement.click()

    def check_honda(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_HONDA)
        checkboxElement.click()

    # Verify if each element has been selected

    def bmw_ischecked(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BMW)
        result = checkboxElement.is_selected()
        if result:
            print('BMW is already selected')
        else:
            print('BMW is not selected')

    def benz_ischecked(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_BENZ)
        result = checkboxElement.is_selected()
        if result:
            print('BENZ is already selected')
        else:
            print('BENZ is not selected')        

    def honda_ischecked(self):
        checkboxElement = self._driver.find_element_by_id(Checkbox.CHECKBOX_HONDA)
        result = checkboxElement.is_selected()
        if result:
            print('HONDA is already selected')
        else:
            print('HONDA is not selected')

    #Select all checkboxes

    def select_all_checkboxes(self):
        Checkbox.check_bmw(self)
        Checkbox.check_benz(self)
        Checkbox.check_honda(self)
        
    #Verify that all checkboxes have been selected

    def verify_all_checkboxes(self):
        Checkbox.bmw_ischecked(self)
        Checkbox.benz_ischecked(self)
        Checkbox.honda_ischecked(self)