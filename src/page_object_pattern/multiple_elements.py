from selenium.webdriver.support.select import Select
from src.page_object_pattern.base_page import BasePage
import pdb

class MultipleElements(BasePage):

    MULTIPLE_SELECT = 'multiple-select-example'

    def multiple_select_all(self):
        """
        Select all elements
        """
        select_all = Select(self._driver.find_element_by_id(MultipleElements.MULTIPLE_SELECT))
        self._driver.find_element_by_id(MultipleElements.MULTIPLE_SELECT).click()
        return select_all.select_all_elements()

    def multiple_select_by_index(self, element_index):
        """
        Enter the index, you want to select
        """
        select_index = Select(self._driver.find_element_by_id(MultipleElements.MULTIPLE_SELECT))
        return select_index.select_by_index(element_index)

    def multiple_select_by_value(self, element_value):
        """
        Enter the value corresponding to the fruit you want to select
        """
        select_value = Select(self._driver.find_element_by_id(MultipleElements.MULTIPLE_SELECT))
        return select_value.select_by_value(element_value)

    def multiple_select_by_text(self, element_text):
        """
        Enter the Fruit that you want to select
        """
        select_text = Select(self._driver.find_element_by_id(MultipleElements.MULTIPLE_SELECT))
        select_text = select_text.select_by_visible_text(element_text)
        return select_text.select_by_visible_text(element_text)