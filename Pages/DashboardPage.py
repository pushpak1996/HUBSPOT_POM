from Tests.BaseClass import SeleniumDriver


class DashboardPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _Reports = "nav-primary-reports-branch"                  #id
    _Dashboard = "nav-secondary-dashboards"                  #id
    _AddReportBtn = '//*[@id="add-report"]/i18n-string'      #xpath
    _AddReportBtn2 = "/html/body/div[2]/div/div/div/div/section/div/div[2]/main/div/div[2]/div[1]/div/div[1]/div/button[1]/span"  #xpath

    _BackToDash = "back-to-dashboard"                        #id
    _VerifyReport = "//button[.='Contacts Created By Day']"  #xpath

    _RemoveReportBtn = "/html/body/div[2]/div/div/div/div/section/div/div[2]/main/div/div[2]/div[1]/div/div[1]/div/button[1]"        #xpath

    def NavigateToreports(self):
        self.elementClick(self._Reports, locatorType="id")
        self.elementClick(self._Dashboard, locatorType="id")

    def CreateReport(self):
        self.elementClick(self._AddReportBtn, locatorType="xpath")
        self.elementClick(self._AddReportBtn2, locatorType="xpath")

    def DeleteReport(self):
        self.elementClick(self._AddReportBtn,locatorType="xpath")
        self.elementClick(self._RemoveReportBtn,locatorType="xpath")

    def VerifyCreateReport(self):
        self.elementClick(self._BackToDash,locatorType="id")
        element = self.getElement(self._VerifyReport, locatorType="xpath")
        return element.text

    def VerifyDeleteReport(self):
        self.elementClick(self._BackToDash,locatorType="id")
        element = self.isElementPresent(self._VerifyReport,locatorType="xpath")
        return element