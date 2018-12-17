from Tests.BaseClass import SeleniumDriver

class DealPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _DealMenu = "nav-primary-sales-branch"                                      #id
    _DealMenuItem = "nav-secondary-deals"                                       #id
    _CreateDealBtn = "button[data-selenium-test='new-object-button']"           #css
    _NameTxt = "input[data-field='dealname']"                                   #css
    _Pipeline = "//label[.='Pipeline']/../div/button"                           #xpath
    _PipelineValue = "button[title = 'Sales Pipeline']"                         #css
    _DealStage = "//label[.='Deal stage']/../div/button"                        #xpath
    _DealStageValue = "button[title='Qualified To Buy']"                        #css
    _AmtTxt = "input[data-field='amount']"                                      #css
    _CreateDealBtn2 = "button[data-selenium-test='base-dialog-confirm-btn']"    #css

    _ActionsMenu = "button[data-selenium-test='profile-settings-actions-btn']"  #css
    _ActionsMenuItem = "i18n-string[data-key='deleteModal.dealButtonText']"     #css
    _Delete= "button[data-selenium-test='delete-dialog-confirm-button']"        #css

    _VerifyCreateDeal = "// input[ @ placeholder = 'Deal Name']"                #xpath

    _SearchDeal = "input[type=search]"                                          #css
    _VerifyDeleteDeal = "h4"                                                    #css

    def NavigateToDeal(self):
        self.elementClick(self._DealMenu, locatorType="id")
        self.elementClick(self._DealMenuItem, locatorType="id")

    def CreateDeal(self, deal_data):
        self.elementClick(self._CreateDealBtn, locatorType="css")
        self.sendKeys(deal_data[0], self._NameTxt, locatorType="css")
        self.elementClick(self._Pipeline,locatorType="xpath")
        self.elementClick(self._PipelineValue,locatorType="css")
        self.elementClick(self._DealStage,locatorType="xpath")
        self.elementClick(self._DealStageValue,locatorType="css")
        self.sendKeys(deal_data[1], self._AmtTxt, locatorType="css")
        self.elementClick(self._CreateDealBtn2, locatorType="css")

    def DeleteDeal(self, deal_data):
        self.elementClick(deal_data[0], locatorType="link")
        self.elementClick(self._ActionsMenu, locatorType="css")
        self.elementClick(self._ActionsMenuItem, locatorType="css")
        self.elementClick(self._Delete, locatorType="css")

    def VerifyCreateDeal(self):
        #element = self.getElement(self._VerifyCreateDeal, locatorType="xpath")
        attr_val = self.getElementAttr(self._VerifyCreateDeal,"value", locatorType="xpath")
        return attr_val

    def VerifyDeleteDeal(self, deal_data):
        self.sendKeys(deal_data[0], self._SearchDeal, locatorType="css")
        element = self.getElement(self._VerifyDeleteDeal, locatorType="css")
        return element.text