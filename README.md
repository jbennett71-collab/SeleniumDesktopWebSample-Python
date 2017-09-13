# Python Web Automation Code Sample

[![CircleCI](https://circleci.com/gh/PerfectoCode/SeleniumDesktopWebSample-Python.svg?style=shield)](https://circleci.com/gh/PerfectoCode/SeleniumDesktopWebSample-Python)

This code sample demonstrates how to use Perfecto Web Machines & Selenium + Python programing language in order to execute tests 
for your web applications on the cloud.
For more information regarding Turbo Web Solution please visit: http://developers.perfectomobile.com/display/PD/Automating+Web-apps+with+Perfecto

### Getting Stated: 
- Clone or download the sample:<br/> `git clone https://github.com/PerfectoCode/SeleniumDesktopWebSample-Python.git`
- Add your Perfecto Lab credentials within the one of the templates files:
```Python
...
token = os.environ['token']
host = os.environ['host']
... 
```
You may want to use env variable for your credentials as demonstrated.

Old school credentials may be used by replacing the security token with username and password (Not available for Turbo Web)
```Python
...
user = os.environ['user']
password = os.environ['password']
...
```
:exclamation:Using old school credentials is not a best practice and is not recommended.

- Note:exclamation: the project contain 2 templates:
    - perfectoFastWebTemplate: template for Perfecto Turbo Web.
    - perfectoFastWebTemplateReporting: template for Perfecto Turbo Web + DigitalZoom Reporting.
- Run the project from your IDE or using command line for example `python PerfectoFastWebTemplate.py`

:exclamation:For Non Turbo Web replace:
```Python
self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub/fast', capabilities)
```
with:
```Python
self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub', capabilities)
```

### Web Capabilities:

- To insure your tests run on Perfecto Web machines on the cloud use the capabilities as demonstrated in the code sample: <br/>
```Python
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
            'token': self.token
        }

        # For old school credentials replace token with:
        # 'user': self.user,
        # 'password': self.password

        self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub/fast', capabilities)
```

- More capabilities are available, read more [here](http://developers.perfectomobile.com/display/PD/Supported+Platforms).

### Perfecto Turbo Web Automation:

Perfecto's Desktop Web environment introduces an accelerated interface to Web Browser automation with its new Turbo web interface. Using this new environment will allow you to connect quicker to the browser "device" you select for automating and testing your web application.

- To enable Turbo Web Automation in this code sample follow the instructions in the link above in order to generate authentication token.
Place the authentication in one of the Turbo Web test's files:
```Python
token = os.environ['token']
host = os.environ['host']
...
self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub/fast', capabilities)
```

### Perfecto DigitalZoom reporting:

Perfecto Reporting is a multiple execution digital report, that enables quick navigation within your latest build execution. Get visibility of your test execution status and quickly identify potential problems with an aggregated report.
Hone-in and quickly explore your test results all within customized views, that include logical steps and synced artifacts. Distinguish between test methods within a long execution. Add personalized logical steps and tags according to your team and organization.

*Click [here](http://developers.perfectomobile.com/display/PD/Reporting) to read more about DigitalZoom Reporting.*
