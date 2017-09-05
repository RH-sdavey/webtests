#!/usr/bin/env python3
#
# Framewor for testing web aplications - proof of concept
# Authors:  Roman Vais <rvais@redhat.com>
#

from selenium.webdriver.remote.webelement import WebElement

class Element(object):

    def __init__(self, webelem: WebElement):
        self._elem = webelem

    def __eq__(self, elem):
        return self._elem == elem._elem

    def __ne__(self, element):
        return not self.__eq__(element)

    # attributes and properties of element -------------------------------------------------
    @property
    def id(self):
        self._elem.id

    @property
    def classname(self):
        return ""

    @property
    def tag_name(self):
        return self._elem.tag_name

    @property
    def text(self):
        return self._elem.text

    @property
    def width(self):
        return self._elem.size["width"]

    @property
    def height(self):
        return self._elem.size["height"]

    @property
    def selected(self):
        return self._elem.is_selected()

    @property
    def enabled(self):
        return self._elem.is_enabled()

    def get_property(self, name: str):
        return self._elem.get_property(name)

    def get_attribute(self, name: str):
        return  self._elem.get_attribute(name)

    def get_size(self):
        return self._elem.size

    def get_css_property_value(self, property_name: str):
        return self._elem.value_of_css_property(property_name)

    # searching for inner elements -------------------------------------------------
    def find_element_by_id(self, id: str):
        return Element(self._elem.find_element_by_id(id))

    def find_elements_by_id(self, id: str):
        element_list = list()
        for elm in self._elem.find_elements_by_id(id):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_class_name(self, classname: str):
        return Element(self._elem.find_element_by_class_name(classname))

    def find_elements_by_class_name(self, classname: str):
        element_list = list()
        for elm in self._elem.find_elements_by_class_name(classname):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_tag_name(self, tagname: str):
        return Element(self._elem.find_element_by_tag_name(tagname))

    def find_elements_by_tag_name(self, tagname: str):
        element_list = list()
        for elm in self._elem.find_elements_by_tag_name(tagname):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_name(self, name: str):
        return Element(self._elem.find_element_by_name(name))

    def find_elements_by_name(self, name: str):
        element_list = list()
        for elm in self._elem.find_elements_by_name(name):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_xpath(self, xpath: str):
        return Element(self._elem.find_element_by_xpath(xpath))

    def find_elements_by_xpath(self, xpath: str):
        element_list = list()
        for elm in self._elem.find_elements_by_xpath(xpath):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_link_text(self, link_text: str):
        return Element(self._elem.find_element_by_link_text(link_text))

    def find_elements_by_link_text(self, link_text: str):
        element_list = list()
        for elm in self._elem.find_elements_by_link_text(link_text):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_partial_link_text(self, link_text: str):
        return Element(self._elem.find_element_by_partial_link_text(link_text))

    def find_elements_by_partial_link_text(self, link_text: str):
        element_list = list()
        for elm in self._elem.find_elements_by_partial_link_text(link_text):
            element_list.append(Element(elm))

        return element_list

    def find_element_by_css_selector(self, css_selector: str):
        return Element(self._elem.find_element_by_css_selector(css_selector))

    def find_elements_by_css_selector(self, css_selector: str):
        element_list = list()
        for elm in self._elem.find_elements_by_css_selector(css_selector):
            element_list.append(Element(elm))

        return element_list

    def get_childnodes(self):
        return self.find_elements_by_xpath('./*')

    # actions performed on element -------------------------------------------------

#    def location_once_scrolled_into_view(self):

    def click(self):
        self._elem.click()

    def submit(self):
        self._elem.submit()

    def clear(self):
        self._elem.clear()

#    def location(self):

#    def screenshot_as_base64(self):

#    def screenshot_as_png(self):

#    def screenshot(self, filename: str):


