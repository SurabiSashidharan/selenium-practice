import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new")
    # drv = webdriver.Chrome(options=options)
    drv = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_b64 = driver.get_screenshot_as_base64()
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.image(screenshot_b64, "Failure Screenshot"))
            report.extras = extras