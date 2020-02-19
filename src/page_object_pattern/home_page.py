"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage


class HomePage(BasePage):
    """
    Home page
    """
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'
    CREATE_ACCOUNT = 'pt-createaccount'
    LOGIN = 'pt-login'
    MAIN_LINK ='ca-nstab-main'

    def set_search_query(self, query: str):
        """
        Search for a string
        :param query: string you are looking for
        """
        self._driver.find_element_by_id(HomePage.SEARCH_CONTAINER).send_keys(query)

    def check_font_main_link(self):
        """
        Check the computed font for an element
        """
        ide = HomePage.MAIN_LINK
        javaScript = "return document.getElementById(arguments[0]);"
        elem = self._driver.execute_script(javaScript, ide)
        print(elem.text)
        font = "font-family"
        font_computed = self._driver.execute_script("return window.getComputedStyle(arguments[0], null).getPropertyValue(arguments[1]);", elem, font)
        print(font_computed)
        fontsize = "font-size"
        font_computed_size = self._driver.execute_script(
            "return window.getComputedStyle(arguments[0], null).getPropertyValue(arguments[1]);", elem, fontsize)
        print(font_computed_size)

        #self._driver.execute_script("$('searchButton').click('')")

        #window.getComputedStyle(elem, null).getPropertyValue("font-family")

    def check_search(self):
        """
        Check search button is visible
        """
        return self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).is_displayed()

    def search(self):
        """
        Click on search button
        """
        self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).click()

    def check_login(self):
        """
        Check Login button is visible
        """
        return self._driver.find_element_by_id(HomePage.LOGIN).is_displayed()

    def login(self):
        """
        Press login button
        """
        self._driver.find_element_by_id(HomePage.LOGIN).click()

    def check_create_account(self):
        """
        Check create account button available
        """
        return self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).is_displayed()

    def create_account(self):
        """
        Press create account button
        """
        self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).click()

