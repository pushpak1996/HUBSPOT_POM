from selenium import webdriver
sys.path.insert(0, "../../HUBSPOT_POM")
from Pages.LoginPage import LoginPage
from Pages.ContactPage import ContactPage
from Pages.TicketPage import TicketPage
from Pages.DealPage import DealPage
from Pages.SnippetPage import SnippetPage
import unittest
import configparser
import sys

class TestClass(unittest.TestCase):
    config = configparser.ConfigParser()  # create an object called config
    config.read('../Test_Config/HS_config.cfg')                       # ../ is to come out from present folder

    ch_executable_path = config.get("Testing", "ch_driver_path")
    ff_executable_path = config.get("Testing", "ff_driver_path")
    me_executable_path = config.get("Testing", "me_driver_path")
    baseURL = config.get("Testing", "hs_url")
    user = config.get("Testing", "hs_un")
    pwd = config.get("Testing", "hs_pwd")
    impwait = config.get("Testing", "implicit_wait")
    browser_type = config.get("Testing", "browser_type")

    def setUp(self):
        global driver, lp, cp, tp, dp, sp

        if self.browser_type.lower() == "ch":
            driver = webdriver.Chrome(self.ch_executable_path)
        elif self.browser_type.lower() == "ff":
            driver = webdriver.Firefox(executable_path=self.ff_executable_path)
        elif self.browser_type.lower() == "me":
            driver = webdriver.Edge(self.me_executable_path)

        driver.maximize_window()
        driver.get(self.baseURL)
        driver.implicitly_wait(self.impwait)

        lp = LoginPage(driver)
        cp = ContactPage(driver)
        tp = TicketPage(driver)
        dp = DealPage(driver)
        sp = SnippetPage(driver)

        lp.UserLogin(self.user,self.pwd)

    def tearDown(self):
        lp.UserLogout()
        driver.quit()

    def test_1_login(self):
        text=lp.VerifyLogin()
        assert text == "Welcome back, PUSHPAK KUMAR."
        print(text)
    
    def test_2_create_contact(self):
        global contact_data
        contact_data = ["james.bond@gmail.com", "James", "Bond", "Test Developer"]
        cp.NavigateToContact()
        cp.CreateContact(contact_data)
        text = cp.VerifyCreateContact()
        assert text == contact_data[1]+" "+contact_data[2]
        print(text)
    
    def test_3_delete_contact(self):
        cp.NavigateToContact()
        cp.DeleteContact(contact_data)
        text = cp.VerifyDeleteContact(contact_data)
        assert text == "No contacts match the current filters."
        print(text)
    
    def test_4_create_ticket(self):
        global ticket_data
        ticket_data = "John"
        tp.NavigateToTicket()
        tp.CreateTicket(ticket_data)
        text = tp.VerifyCreateTicket()
        assert text == ticket_data
        print(text)
    
    def test_5_delete_contact(self):
        tp.NavigateToTicket()
        ticket_data = "John"
        tp.DeleteTicket(ticket_data)
        text = tp.VerifyDeleteTicket(ticket_data)
        assert text == "No tickets could be found."
        print(text)
    
    def test_6_create_deal(self):
        global deal_data
        deal_data = ['John','30000']
        dp.NavigateToDeal()
        dp.CreateDeal(deal_data)
        text = dp.VerifyCreateDeal()
        assert text == deal_data[0]
        print(text)
    
    def test_7_delete_deal(self):
        deal_data = ['John', '30000']
        dp.NavigateToDeal()
        dp.DeleteDeal(deal_data)
        text = dp.VerifyDeleteDeal(deal_data)
        assert text == "No deals match the current filters."
        print(text)
    
    def test_8_create_snippet(self):
        global snippet_data
        snippet_data = ['Confirmation','We will Contact you later.','st']
        sp.NavigateToSnippet()
        sp.CreateSnippet(snippet_data)
        text = sp.VerifyCreateSnippet(snippet_data)
        assert text == snippet_data[0]
        print(text)
    
    def test_9_delete_snippet(self):
        sp.NavigateToSnippet()
        sp.DeleteSnippet(snippet_data)
        text = sp.VerifyDeleteSnippet()
        assert text == "Nothing matches your search."
        print(text)
