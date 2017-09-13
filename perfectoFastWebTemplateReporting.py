import unittest, os
from selenium import webdriver
from perfecto import *

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
        self.host = host
        self.driver = None
        self.reporting_client = None
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
            'securityToken': self.token,
        }

        # For Regular web (physical devices) remove the '/fast' at the end of the Url (Please check the README file for more information)
        self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub/fast', capabilities)

        self.create_reporting_client()
        self.reporting_client.test_start(self.id(),
                                         TestContext('Tag1', 'Tag2', 'Tag3'))

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
        self.reporting_client.step_start("Navigate to google")
        self.driver.get('https://www.google.com')
        self.reporting_client.step_end()

        ###########################
        # Complete your test here #
        ###########################

    def tearDown(self):
        """
        Tear down method
        responsible for pass to Reporting DigitalZoom the test status succeed or either failed
        :return: 
        """
        try:
            if self.currentResult.wasSuccessful():
                self.reporting_client.test_stop(TestResultFactory.create_success())
            else:
                self.reporting_client.test_stop(TestResultFactory.create_failure(self.currentResult.errors,
                                                                                 self.currentResult.failures))
            # Print report's url
            print 'Report-Url: ' + self.reporting_client.report_url() + '\n'
        except Exception as e:
            print e.message

        self.driver.quit()

    def create_reporting_client(self):
        perfecto_execution_context = PerfectoExecutionContext(webdriver=self.driver,
                                                              context_tags=['Python', 'Desktop Web'],
                                                              job=Job('JobName', 1),
                                                              project=Project('DesktopWeb', '0.1'))
        self.reporting_client = PerfectoReportiumClient(perfecto_execution_context)

unittest.main()
