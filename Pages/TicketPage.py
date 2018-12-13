from Tests.BaseClass import SeleniumDriver
# from Tests.TestClass import TestClass as TC

class TicketPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _ServiceMenu = "nav-primary-service-branch"                                                 #id
    _TicketsMenuItem = "nav-secondary-tickets"                                                  #id
    _CreateTicketBtn = "//span[.='Create ticket']"                                              #xpath

    _Ticketname = "input[data-field='subject']"                                                 #css
    _Pipeline = "//label[.='Pipeline']/../div/button"                                           #xpath
    _PipelineValue = "button[title = 'Support Pipeline']"                                       #css
    _TicketStatus = "//label[.='Ticket status']/../div/button"                                  #xpath # /.. means go to parent and /div come to sibling
    _TicketStatusVal = "button[title='New']"                                                    #css
    _CreateTicketBtn2 = "button[data-selenium-test='base-dialog-confirm-btn']"                  #css

    _ActionsMenu = "button[data-selenium-test='profile-settings-actions-btn']"                  #css
    _ActionsMenuItem = "button[data-selenium-test='profile-settings-profileSettings.delete']"   #css
    _Delete = "i18n-string[data-key='deleteModal.buttonText']"                                  #css

    _VerifyCreate = "h2>div>div>span>span>span>span"                                            #css

    _SearchTicket = "input[type = 'search']"                                                    #css
    _VerifyDelete = "h4"                                                                        #css

    def NavigateToTicket(self):
        self.elementClick(self._ServiceMenu, locatorType="id")
        self.elementClick(self._TicketsMenuItem, locatorType="id")

    def CreateTicket(self, ticket_data):
        self.elementClick(self._CreateTicketBtn,locatorType="xpath")
        # self.executeJS("document.getElementsByTagName('button')[1].click();")
        self.sendKeys(ticket_data,self._Ticketname,locatorType="css")
        self.elementClick(self._Pipeline,locatorType="xpath")
        self.elementClick(self._PipelineValue,locatorType="css")
        self.elementClick(self._TicketStatus,locatorType="xpath")
        self.elementClick(self._TicketStatusVal,locatorType="css")
        self.elementClick(self._CreateTicketBtn2,locatorType="css")

    def DeleteTicket(self, ticket_data):
        self.elementClick(ticket_data, locatorType="link")
        self.elementClick(self._ActionsMenu,locatorType="css")
        self.elementClick(self._ActionsMenuItem,locatorType="css")
        self.elementClick(self._Delete,locatorType="css")

    def VerifyCreateTicket(self):
        element = self.getElement(self._VerifyCreate, locatorType="css")
        return element.text

    def VerifyDeleteTicket(self,ticket_data):
        self.sendKeys(ticket_data,self._SearchTicket,locatorType="css")
        element = self.getElement(self._VerifyDelete, locatorType="css")
        return element.text