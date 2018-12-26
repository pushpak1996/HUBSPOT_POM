from Tests.BaseClass import SeleniumDriver


class CompanyPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _ContactMenu = "nav-primary-contacts-branch"                                          #id
    _ContactMenuItem = "nav-secondary-companies"                                          #id
    _CreateCompanyBtn = "button[data-onboarding='new-object-button']"                     #css
    _CompanyDomain = "input[data-field='domain']"                                         #css
    _GetName = "input[data-field='name']"                                                 #css
    _CreateCompanyBtn2 = "button[data-selenium-test='base-dialog-confirm-btn']"           #css

    _ActionsMenu = "button[data-selenium-test='profile-settings-actions-btn']"            #css
    _ActionsMenuItem = "i18n-string[data-key='profileSettings.delete']"                   #css
    _Delete = "i18n-string[data-key='deleteModal.buttonText']"                            #css

    _VerifyCreate = "h2>div>div>span>span>span>span"                                      #css

    _SearchCompany = "input[type=search]"                                                 #css
    _VerifyDelete = "h4"                                                                  #css

    def NavigateToCompany(self):
        self.elementClick(self._ContactMenu, locatorType="id")
        self.elementClick(self._ContactMenuItem, locatorType="id")

    def CreateCompany(self, company_data):
        self.elementClick(self._CreateCompanyBtn, locatorType="css")
        self.sendKeys(company_data,self._CompanyDomain,locatorType="css")
        attr_val = self.getElementAttr(self._GetName,"value", locatorType="css")
        self.elementClick(self._CreateCompanyBtn2,locatorType="css")
        return attr_val

    def DeleteCompany(self, name):
        self.elementClick(name, locatorType="link")
        self.elementClick(self._ActionsMenu,locatorType="css")
        self.elementClick(self._ActionsMenuItem,locatorType="css")
        self.elementClick(self._Delete,locatorType="css")

    def VerifyCreateCompany(self):
        element = self.getElement(self._VerifyCreate, locatorType="css")
        return element.text

    def VerifyDeleteCompany(self, company_data):
        self.sendKeys(company_data, self._SearchCompany, locatorType="css")
        element = self.getElement(self._VerifyDelete, locatorType="css")
        return element.text