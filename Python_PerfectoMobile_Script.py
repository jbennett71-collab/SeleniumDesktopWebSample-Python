import time
import csv
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# ======================== CONFIGURATION SECTION ========================

cloud_name = "demo"
security_token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiw...NDkyMGYifQ.eizwYjNGtOiNTHrkR7WcRX9RcFlgXmzjseJsN02rYgE"

app_path_android = "PUBLIC:ExpenseTracker/Native/ExpenseAppVer1.0.apk"
app_path_ios = "PUBLIC:ExpenseTracker/Native/InvoiceApp1.0.ipa"

app_package = "io.perfecto.expense.tracker"
bundle_id = "io.perfecto.expense.tracker"

csv_file_path = "C:/Windows/Users/Jbenn/myprojects/credentials.csv"

# ======================== UTILITY FUNCTIONS ========================

def read_credentials_from_csv(file_path):
    credentials = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            credentials.append({
                "username": row.get("username"),
                "password": row.get("password")
            })
    return credentials

def create_driver(platform):
    command_executor_url = f"https://{cloud_name}.perfectomobile.com/nexperience/wd/hub"

    capabilities = {
        "platformName": "Android" if platform.lower() == "android" else "iOS",
        "model": "Galaxy.*" if platform.lower() == "android" else "iPhone.*",
        "app": app_path_android if platform.lower() == "android" else app_path_ios,
        "perfecto:securityToken": security_token,
        "sensorInstrument": True,
        "useAppiumForWeb": True,
        "autoLaunch": True
    }

    if platform.lower() == "android":
        capabilities.update({
            "automationName": "UiAutomator2",
            "appPackage": app_package,
            "deviceName": "AndroidDevice"
        })
    elif platform.lower() == "ios":
        capabilities.update({
            "automationName": "XCUITest",
            "bundleId": bundle_id,
            "deviceName": "iOSDevice"
        })
    else:
        raise Exception("Unsupported platform")

    print(f"\n--- Connecting to {platform} device ---")
    print("Command Executor URL:", command_executor_url)
    print("Capabilities:", capabilities)

    driver = webdriver.Remote(command_executor=command_executor_url, desired_capabilities=capabilities)
    return driver

def perform_login(driver, username, password):
    print(f"Trying to login with {username} / {password}")
    try:
        time.sleep(3)
        driver.find_element("accessibility id", "username").send_keys(username)
        driver.find_element("accessibility id", "password").send_keys(password)
        driver.find_element("accessibility id", "login").click()
        time.sleep(3)

        try:
            driver.find_element("accessibility id", "loginError")
            print("Login failed as expected.")
            return False
        except NoSuchElementException:
            print("Login may have succeeded.")
            return True
    except Exception as e:
        print("Error during login:", e)
        return False

def verify_login_success(driver):
    try:
        driver.find_element("accessibility id", "menu")
        print("✅ Login successful checkpoint passed.")
        return True
    except NoSuchElementException:
        print("❌ Login failed checkpoint.")
        return False

def crash_the_app(driver):
    try:
        driver.find_element("accessibility id", "menu").click()
        time.sleep(1)
        driver.find_element("accessibility id", "About").click()
        time.sleep(1)
        driver.execute_script('mobile:terminateApp', {'bundleId': bundle_id})
        print("💥 App crashed deliberately.")
    except Exception as e:
        print("Error while crashing the app:", e)

def run_test_on_platform(platform):
    print(f"\n===== Running login test on {platform} ======")
    driver = create_driver(platform)
    time.sleep(5)

    credentials = read_credentials_from_csv(csv_file_path)

    for cred in credentials:
        driver.launch_app()
        result = perform_login(driver, cred['username'], cred['password'])

        if cred['username'] == "test@perfecto.com":
            assert result and verify_login_success(driver), "Final valid login should succeed"
            crash_the_app(driver)
        else:
            assert not result, "Invalid login should fail"
            driver.reset()

    try:
        report_url = driver.capabilities.get('reportPdfUrl') or driver.capabilities.get('reportUrl')
        if report_url:
            print(f"📄 Perfecto Report URL: {report_url}")
        else:
            print("⚠️ No report URL found in capabilities.")
    except Exception as e:
        print("⚠️ Error retrieving Perfecto report URL:", e)

    driver.quit()

# ======================== MAIN ENTRY POINT ========================

if __name__ == "__main__":
    run_test_on_platform("Android")
    run_test_on_platform("iOS")