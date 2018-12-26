from Tests.BaseClass import SeleniumDriver
from selenium import webdriver
from Tests.HS_TestData import TestData


class TemplatePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _Conversation = "nav-primary-conversations-branch"                                                     #id
    _Templates = "nav-secondary-templates"                                                                 #id
    _NewTemplateBtn = "button[data-button-use='primary']"                                                  #css
    _NewTemplateVal = "//i18n-string[.='From scratch']"                                                    #xpath
    _Name = "//div[@class='template-editor']/div/input"                                                    #xpath
    _Subject = "//div[@class='subject-block']"                                                             #xpath
    _Body = "//div[3]/div/div/div[@class='DraftEditor-root']"                                              #xpath
    _SaveTemplate = "//span[.='Save template']"                                                            #xpath
    _Search = "input[type='search']"                                                                       #css
    _Templatelink = "//a[contains(text(),'"+TestData.template_data[0]+"')]"                                #xpath
    _DeleteTemplate = "//span[.='Delete']"                                                                 #xpath
    _ConfirmDelete = "button[data-selenium-test='delete-confirm-button']"                                  #css
    _VerifyDelete = "i18n-string[data-key='salesContentIndexUI.emptyState.search.nothingMatchesSearch']"   #css
    _Checkbox = "//a[contains(text(),'"+TestData.template_data[0]+"')]/../../../../../../../td[1]/div/div/label/span/span"  #xpath

    def NavigateToTemplate(self):
        self.elementClick(self._Conversation, locatorType="id")
        self.elementClick(self._Templates, locatorType="id")

    def CreateTemplate(self, template_data):
        self.elementClick(self._NewTemplateBtn, locatorType="css")
        self.elementClick(self._NewTemplateVal, locatorType="xpath")
        self.sendKeys(template_data[0], self._Name, locatorType="xpath")
        self.driver.find_element_by_xpath(self._Subject).click()
        webdriver.ActionChains(self.driver).send_keys(template_data[1]).perform()
        self.driver.find_element_by_xpath(self._Body).click()
        webdriver.ActionChains(self.driver).send_keys(template_data[2]).perform()
        self.elementClick(self._SaveTemplate, locatorType="xpath")

    def VerifyCreate(self, template_data):
        self.sendKeys(template_data[0], self._Search, locatorType="css")
        element = self.getElement(self._Templatelink, locatorType="xpath")
        return element.text

    def DeleteTemplate(self, template_data):
        self.sendKeys(template_data[0], self._Search, locatorType="css")
        self.elementClick(self._Checkbox, locatorType="xpath")
        self.elementClick(self._DeleteTemplate, locatorType="xpath")
        self.elementClick(self._ConfirmDelete, locatorType="css")

    def VerifyDelete(self):
        element = self.getElement(self._VerifyDelete, locatorType="css")
        return element.text