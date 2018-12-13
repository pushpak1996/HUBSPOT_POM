from Tests.BaseClass import SeleniumDriver


class ContactPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _ContactMenu = "nav-primary-contacts-branch"                                   #id
    _ContactMenuItem = "nav-secondary-contacts"                                    #id
    _CreateContactBtn = "button[data-button-use='primary']"                        #css
    _EmailTxt = "input[data-field='email']"                                        #css
    _FirstNameTxt = "input[data-field='firstname']"                                #css
    _LastNameTxt = "input[data-field='lastname']"                                  #css
    _jobTitleTxt = "input[data-field='jobtitle']"                                  #css
    _CreateContactBtn2 = "button[data-selenium-test='base-dialog-confirm-btn']"    #css

    _ActionsMenu = "button[data-selenium-test='profile-settings-actions-btn']"     #css
    _ActionsMenuItem = "i18n-string[data-key='profileSettings.delete']"            #css
    _Delete = "i18n-string[data-key='deleteModal.buttonText']"                     #css

    _VerifyCreate = "h2>div>div>span>span>span>span"                               #css

    _SearchContact = "input[type=search]"                                          #css
    _VerifyDelete = "h4"                                                           #css

    def NavigateToContact(self):
        self.elementClick(self._ContactMenu, locatorType="id")
        self.elementClick(self._ContactMenuItem, locatorType="id")

    def CreateContact(self, contact_data):
        self.elementClick(self._CreateContactBtn, locatorType="css")
        self.sendKeys(contact_data[0],self._EmailTxt,locatorType="css")
        self.sendKeys(contact_data[1],self._FirstNameTxt,locatorType="css")
        self.sendKeys(contact_data[2],self._LastNameTxt,locatorType="css")
        self.sendKeys(contact_data[3],self._jobTitleTxt,locatorType="css")
        self.elementClick(self._CreateContactBtn2,locatorType="css")

    def DeleteContact(self, contact_data):
        self.elementClick(contact_data[1]+" "+contact_data[2], locatorType="link")
        self.elementClick(self._ActionsMenu,locatorType="css")
        self.elementClick(self._ActionsMenuItem,locatorType="css")
        self.elementClick(self._Delete,locatorType="css")

    def VerifyCreateContact(self):
        element = self.getElement(self._VerifyCreate, locatorType="css")
        return element.text

    def VerifyDeleteContact(self, contact_data):
        self.sendKeys(contact_data[1]+" "+contact_data[2], self._SearchContact, locatorType="css")
        element = self.getElement(self._VerifyDelete, locatorType="css")
        return element.text