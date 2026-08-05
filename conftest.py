import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture
def driver():
    drv = webdriver.Chrome()
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