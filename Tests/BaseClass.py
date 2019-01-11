from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#import UtilityPackage.CustomLogger as cl
import logging
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import os


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            self.capture_screenshot()

    def elementClick(self, locator, locatorType="id"):
        try:

            element = self.getElement(locator, locatorType)

            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()
            self.capture_screenshot()

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            time.sleep(3)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            self.capture_screenshot()
        return element

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME
        else:
            print("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def executeJS(self,js):
        time.sleep(5)
        self.driver.execute_script(js)
        print("Executed JS "+js)

    def getElementAttr(self, locator, attr, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            time.sleep(3)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            self.capture_screenshot()
        attr_val = element.get_attribute(attr)
        return attr_val

    def isElementPresent(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            time.sleep(3)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                  " and  locatorType: " + locatorType)
            return True
        except:
            print("Element not found with locator: " + locator +
                  " and  locatorType: " + locatorType)
            self.capture_screenshot()
            return False

    def capture_screenshot(self):
        sp_time = datetime.datetime.now()
        spt = sp_time.strftime('%d-%m-%y_%H-%M-%S')
        file_path = '../Snapshots/HS_'+spt+'.png'
        self.driver.save_screenshot(file_path)