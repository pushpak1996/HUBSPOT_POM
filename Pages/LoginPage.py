from Tests.BaseClass import SeleniumDriver

"""
LoginToGithub class : Page class which contains all the methods and variables. 
All the methods can be re-used by creating object of this class and calling as object.method()
to execute the test case.
Methods defined here are used in TestClass to validate the github login functionality.
"""

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators in login page for hubspot                  #Locator types for reference
    _EmailField = "username"                              #id
    _PasswordField = "password"                           #id
    _SignInButton = "loginBtn"                            #id
    _VerifyLogin = "span[data-locale-at-render='en-gb']"  #css

    _Logout = "img[class=' nav-avatar ']"                 #css
    _Signout = "signout"                                  #id

    def UserLogin(self, email, password):
        self.sendKeys(email, self._EmailField, locatorType="id")
        self.sendKeys(password, self._PasswordField, locatorType="id")
        self.elementClick(self._SignInButton, locatorType="id")

    def VerifyLogin(self):
        element = self.getElement(self._VerifyLogin, locatorType="css")
        return element.text

    def UserLogout(self):
        self.elementClick(self._Logout,locatorType="css")
        self.elementClick(self._Signout,locatorType="id")