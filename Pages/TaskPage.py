from Tests.BaseClass import SeleniumDriver


class TaskPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _TaskMenu = "nav-primary-sales-branch"                                                       #id
    _TaskMenuItem = "nav-secondary-tasks"                                                        #id
    _CreateTaskBtn = "button[data-selenium-test='TasksHeaderView__add-task-btn']"                #css
    _TitleText = "input[data-selenium-test='TaskPropertyTitleInput__task-name-input']"           #css
    _ClickBtn = "button[data-selenium-test='CreateTaskSidebar__save-btn']"                       #css

    _Delete = "//span[.='Open']/../../../../../../../../../../../../td[1]/div/label/span/span"   #xpath
    _DeleteBtn = "button[data-selenium-test='TasksTopbarBulkActions__delete-btn']"               #css
    _DeleteBtn2 = "button[data-selenium-test='delete-dialog-confirm-button']"                    #css

    _CreateSearch = "input[type='search']"                                                       #css
    _VerifyCreateTask = "//a/span/span/span[.='Open']"                                           #xpath

    _VerifyDeleteTask = "h4"                                                                     #css

    def NavigateToTask(self):
        self.elementClick(self._TaskMenu, locatorType="id")
        self.elementClick(self._TaskMenuItem, locatorType="id")

    def CreateTask(self, task_data):
        self.elementClick(self._CreateTaskBtn, locatorType="css")
        self.sendKeys(task_data, self._TitleText, locatorType="css")
        self.elementClick(self._ClickBtn, locatorType="css")

    def DeleteTask(self):
        self.elementClick(self._Delete, locatorType="xpath")
        self.elementClick(self._DeleteBtn, locatorType="css")
        self.elementClick(self._DeleteBtn2, locatorType="css")

    def VerifyCreateTask(self):
        element = self.getElement(self._VerifyCreateTask, locatorType="xpath")
        return element.text

    def VerifyDeleteTask(self, task_data):
        self.sendKeys(task_data, self._CreateSearch, locatorType="css")
        element = self.getElement(self._VerifyDeleteTask, locatorType="css")
        return element.text











