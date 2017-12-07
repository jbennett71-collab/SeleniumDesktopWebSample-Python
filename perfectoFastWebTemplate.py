import unittest, os
from selenium import webdriver

token = os.environ['token']
host = os.environ['host']


class TestWeb(unittest.TestCase):
    """
    Perfecto Desktop Web Using Selenium WebDriver:
    This project demonstrate simply how to open a Desktop Web
    machine within your Perfecto Lab in the cloud and running your tests
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize test suite instance
        :param args: 
        :param kwargs: 
        """
        self.driver = None
        self.currentResult = None

        super(TestWeb, self).__init__(*args, **kwargs)

    def setUp(self):
        """
        Setup method runs before each test
        :return: 
        """
        capabilities = {
            'platformName': 'Windows',
            'platformVersion': '10',
            'browserName': 'Chrome',
            'browserVersion': 'latest',
            'resolution': '1280x1024',
            'securityToken': token,
        }

        # For Regular web (physical devices) remove the '/fast' at the end of the Url (Please check the README file for more information)
        self.driver = webdriver.Remote('https://' + host + '/nexperience/perfectomobile/wd/hub/fast', capabilities)

    def run(self, result=None):
        """
        Overriding run method in order to save the current test result
        :param result: current test status
        :return: 
        """
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method

    def test_webdriver(self):
        """
        Test method
        Complete here your test
        :return: 
        """
        print 'Run started'
        self.driver.get('https://www.google.com')

        ###########################
        # Complete your test here #
        ###########################

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
