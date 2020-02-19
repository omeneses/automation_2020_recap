"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage


class Practice(BasePage):
    """
    Home page
    """
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'
    CREATE_ACCOUNT = 'pt-createaccount'
    LOGIN = 'pt-login'
    MAIN_LINK ='ca-nstab-main'
    RADIO_SECTION_TEXT = '//*[@id="radio-btn-example"]/fieldset/legend'

    def get_title_text(self):
        return self._driver.find_element_by_xpath(Practice.RADIO_SECTION_TEXT).text

    