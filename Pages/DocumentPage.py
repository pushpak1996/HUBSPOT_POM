from Tests.BaseClass import SeleniumDriver
from pywinauto import keyboard
# from pathlib import Path
import time
import os


class DocumentPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _DocMenu = "nav-primary-sales-branch"                                                                               #id
    _DocMenuItem = "nav-secondary-documents"                                                                            #id

    _CreateBtn = "button[data-selenium-test='index-upload-document-test']"                                              #css
    _LocalFile = "//i18n-string[.='Local file']"                                                                        #xpath
    _Delete = "i18n-string[data-key='table.actionButtons.delete']"                                                      #css
    _DeleteBtn = "button[data-selenium-test='confirm-delete-document-button']"                                          #css

    _Search = "input[type='search']"                                                                                    #css

    # doc_path = "G:/Test_Data/questions.xlsx"
    # file_path = Path(doc_path)
    # list = doc_path.split("/")
    # verifyitem = list[2]

    rel_path = "../Test_Data/HS_Test_data.xlsx"
    abs_path = os.path.abspath(rel_path)
    file = rel_path.split("/")
    verifyfile = file[2]

    _VerifyCreate = "//a/span/span/span[.='" + verifyfile + "']"                                                        #xpath
    _CheckboxResume = "//span[.='" + verifyfile + "']/../../../../../../../../../../../td[1]/div/div/label/span/span"   #xpath

    _VerifyDelete = "i18n-string[data-key='salesContentIndexUI.emptyState.search.nothingMatchesSearch']"                #css


    def NavigateToDocument(self):
        self.elementClick(self._DocMenu, locatorType="id")
        self.elementClick(self._DocMenuItem, locatorType="id")

    def CreateDocument(self):
        self.elementClick(self._CreateBtn, locatorType="css")
        self.elementClick(self._LocalFile, locatorType="xpath")
        time.sleep(3)
        keyboard.SendKeys(self.abs_path)
        keyboard.SendKeys('{ENTER}')

    def DeleteDocument(self):
        self.elementClick(self._CheckboxResume, locatorType="xpath")
        self.elementClick(self._Delete, locatorType="css")
        self.elementClick(self._DeleteBtn, locatorType="css")

    def VerifyCreate(self):
        time.sleep(30)
        self.sendKeys(self.file[2], self._Search, locatorType="css")
        element = self.getElement(self._VerifyCreate, locatorType="xpath")
        return element.text

    def VerifyDelete(self):
        self.sendKeys(self.file[2], self._Search, locatorType="css")
        element = self.getElement(self._VerifyDelete, locatorType="css")
        return element.text