#!/usr/bin/env python3
#
# Framewor for testing web aplications - proof of concept 
# Authors:  Roman Vais <rvais@redhat.com>
#

from webtest.components.pagemodel.model import PageModel
from webtest.components.pagemodel.element import Element
from webtest.common.logger import get_logger

class Page(object):

    ROOT_XPATH = '/html'
    ROOT_COMPONENT_NAME = 'root_element'

    def __init__(self, browser: 'Browser', model: PageModel=None):
        class_name = str(self.__class__.__name__)
        self._logger = get_logger(class_name)

        if browser is not None :
            self._browser = browser
            raw_root = browser.driver.find_element_by_xpath(Page.ROOT_XPATH)
            self._root = Element(raw_root)
            
        else:
            self._browser = None
            
        self._model = model

        if self._model is None or model.url != browser.current_url:
            self._model = PageModel()

    def __before_returning_element(self, getter):
        pass

    def get_root(self):
        self.__before_returning_element(self._root)
        return self._root

    def get_component(self, component_name: str=ROOT_COMPONENT_NAME, subcomponent_namestr: str=None):
        if component_name == Page.ROOT_COMPONENT_NAME:
            return self.get_root()

        c = self._model[component_name]
        c.set_root(self.get_root())
        return c




































