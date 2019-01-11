from selenium import webdriver
import sys                                            # this should be first, used to run test through batch file
sys.path.insert(0, "../")                             # this should be before the pages
from Pages.LoginPage import LoginPage
from Pages.ContactPage import ContactPage
from Pages.TicketPage import TicketPage
from Pages.DealPage import DealPage
from Pages.SnippetPage import SnippetPage
from Pages.CompanyPage import CompanyPage
from Pages.DocumentPage import DocumentPage
from Pages.DashboardPage import DashboardPage
from Pages.TaskPage import TaskPage
from Pages.TemplatePage import TemplatePage
from Tests.HS_TestData import TestData
import unittest
import configparser
import datetime


class TestClass(unittest.TestCase):
    config = configparser.ConfigParser()                           # create an object called config
    config.read('../Test_Config/HS_config.cfg')                    # ../ is to come out from present folder

    ch_executable_path = config.get("Testing", "ch_driver_path")
    ff_executable_path = config.get("Testing", "ff_driver_path")
    me_executable_path = config.get("Testing", "me_driver_path")
    baseURL = config.get("Testing", "hs_url")
    user = config.get("Testing", "hs_un")
    pwd = config.get("Testing", "hs_pwd")
    impwait = config.get("Testing", "implicit_wait")

    runtime = datetime.datetime.now().time().hour

    def setUp(self):

        global driver, lp, cp, tp, dp, sp, cmp, dcp, dshp, tsp, tmp

        if (self.runtime % 2) == 0:
            driver = webdriver.Chrome(self.ch_executable_path)
        else:
            driver = webdriver.Firefox(executable_path=self.ff_executable_path)

        driver.maximize_window()
        driver.get(self.baseURL)
        driver.implicitly_wait(self.impwait)

        lp = LoginPage(driver)
        cp = ContactPage(driver)
        tp = TicketPage(driver)
        dp = DealPage(driver)
        sp = SnippetPage(driver)
        cmp = CompanyPage(driver)
        dcp = DocumentPage(driver)
        dshp = DashboardPage(driver)
        tsp = TaskPage(driver)
        tmp = TemplatePage(driver)

        lp.UserLogin(self.user,self.pwd)

    def tearDown(self):
        lp.UserLogout()
        title = driver.title
        assert title == "HubSpot Login"
        print(title)
        driver.quit()

    def test_01_login(self):
        text=lp.VerifyLogin()
        assert text == "Getting started with HubSpot"
        print(text)

    def test_02_create_contact(self):
        # cp.NavigateToContact()
        cp.CreateContact(TestData.contact_data)
        text = cp.VerifyCreateContact()
        assert text == TestData.contact_data.cell(1, 1).value+" "+TestData.contact_data.cell(1, 2).value
        print(text)

    def test_03_delete_contact(self):
        cp.NavigateToContact()
        cp.DeleteContact(TestData.contact_data)
        text = cp.VerifyDeleteContact(TestData.contact_data)
        assert text == "No contacts match the current filters."
        print(text)

    def test_04_create_ticket(self):
        tp.NavigateToTicket()
        tp.CreateTicket(TestData.ticket_data)
        text = tp.VerifyCreateTicket()
        assert text == TestData.ticket_data.cell(1, 0).value
        print(text)

    def test_05_delete_ticket(self):
        tp.NavigateToTicket()
        tp.DeleteTicket(TestData.ticket_data)
        text = tp.VerifyDeleteTicket(TestData.ticket_data)
        assert text == "No tickets could be found."
        print(text)

    def test_06_create_deal(self):
        dp.NavigateToDeal()
        dp.CreateDeal(TestData.deal_data)
        text = dp.VerifyCreateDeal()
        assert text == TestData.deal_data.cell(1, 0).value
        print(text)

    def test_07_delete_deal(self):
        dp.NavigateToDeal()
        dp.DeleteDeal(TestData.deal_data)
        text = dp.VerifyDeleteDeal(TestData.deal_data)
        assert text == "No deals match the current filters."
        print(text)

    def test_08_create_snippet(self):
        sp.NavigateToSnippet()
        sp.CreateSnippet(TestData.snippet_data)
        text = sp.VerifyCreateSnippet(TestData.snippet_data)
        assert text == TestData.snippet_data.cell(1, 0).value
        print(text)

    def test_09_delete_snippet(self):
        sp.NavigateToSnippet()
        sp.DeleteSnippet(TestData.snippet_data)
        text = sp.VerifyDeleteSnippet()
        assert text == "Nothing matches your search."
        print(text)

    def test_10_create_company(self):
        global name
        cmp.NavigateToCompany()
        name = cmp.CreateCompany(TestData.company_data)
        text = cmp.VerifyCreateCompany()
        assert text == name
        print(text)

    def test_11_delete_company(self):
        cmp.NavigateToCompany()
        cmp.DeleteCompany(name)
        text = cmp.VerifyDeleteCompany(TestData.company_data)
        assert text == "No companies match the current filters."
        print(text)

    def test_12_create_document(self):
        dcp.NavigateToDocument()
        dcp.CreateDocument(TestData.abs_path)
        text = dcp.VerifyCreate(TestData.verifyfile)
        assert text == TestData.verifyfile
        print(text)

    def test_13_delete_document(self):
        dcp.NavigateToDocument()
        dcp.DeleteDocument()
        text = dcp.VerifyDelete(TestData.verifyfile)
        assert text == "Nothing matches your search."
        print(text)

    def test_14_create_task(self):
        tsp.NavigateToTask()
        tsp.CreateTask(TestData.task_data)
        text = tsp.VerifyCreateTask()
        assert text == TestData.task_data.cell(1, 0).value
        print(text)

    def test_15_delete_task(self):
        tsp.NavigateToTask()
        tsp.DeleteTask()
        text = tsp.VerifyDeleteTask(TestData.task_data)
        assert text == "No tasks match the current filters."
        print(text)

    def test_16_create_template(self):
        tmp.NavigateToTemplate()
        tmp.CreateTemplate(TestData.template_data)
        text = tmp.VerifyCreate(TestData.template_data)
        assert text == TestData.template_data.cell(1, 0).value
        print(text)

    def test_17_delete_template(self):
        tmp.NavigateToTemplate()
        tmp.DeleteTemplate(TestData.template_data)
        text = tmp.VerifyDelete()
        assert text == "Nothing matches your search."
        print(text)

    def test_18_create_report(self):
        dshp.NavigateToreports()
        dshp.CreateReport()
        text = dshp.VerifyCreateReport()
        assert text == "Contacts Created By Day"
        print(text)

    def test_19_delete_report(self):
        dshp.NavigateToreports()
        dshp.DeleteReport()
        text = dshp.VerifyDeleteReport()
        assert text == False
        print(text)