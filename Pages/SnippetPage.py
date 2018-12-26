from Tests.BaseClass import SeleniumDriver


class SnippetPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _Conversation = "nav-primary-conversations-branch"                                                     #id
    _Snippets = "nav-secondary-snippets"                                                                   #id
    _CreateSnippetBtn = "button[data-selenium-test='create-snippet-button']"                               #css
    _Name = "input[data-selenium-test='snippet-name-input']"                                               #css
    _TextSnippet = "div[class*='DraftEditor'][role='textbox']"                                             #css
    _Shortcut = "input[data-selenium-test='snippet-shortcut-input']"                                       #css
    _SaveSnippet = "button[data-selenium-test='snippet-save-button']"                                      #css

    _CheckBox = "//input[@type='checkbox']/../span/span[2]"                                                #xpath
    _DeleteSnippet = "i18n-string[data-key='table.actionButtons.delete']"                                  #css
    _ConfirmDelete = "button[data-selenium-test='confirm-delete-snippet-button']"                          #css

    _SearchSnippet = "input[type='search']"                                                                #css
    _SnippetLink = "a[role='button']"                                                                      #css

    _VerifyDelete = "i18n-string[data-key='salesContentIndexUI.emptyState.search.nothingMatchesSearch']"   #css

    def NavigateToSnippet(self):
        self.elementClick(self._Conversation, locatorType="id")
        self.elementClick(self._Snippets, locatorType="id")

    def CreateSnippet(self, snippet_data):
        self.elementClick(self._CreateSnippetBtn, locatorType="css")
        self.sendKeys(snippet_data[0], self._Name, locatorType="css")
        self.sendKeys(snippet_data[1], self._TextSnippet, locatorType="css")
        self.sendKeys(snippet_data[2], self._Shortcut, locatorType="css")
        self.elementClick(self._SaveSnippet, locatorType="css")

    def DeleteSnippet(self, snippet_data):
        self.sendKeys(snippet_data[0], self._SearchSnippet, locatorType="css")
        self.elementClick(self._CheckBox, locatorType="xpath")
        self.elementClick(self._DeleteSnippet, locatorType="css")
        self.elementClick(self._ConfirmDelete, locatorType="css")

    def VerifyCreateSnippet(self, snippet_data):
        self.sendKeys(snippet_data[0],self._SearchSnippet,locatorType="css")
        element = self.getElement(self._SnippetLink,locatorType="css")
        return element.text

    def VerifyDeleteSnippet(self):
        element = self.getElement(self._VerifyDelete,locatorType="css")
        return element.text