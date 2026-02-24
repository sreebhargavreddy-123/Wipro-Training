import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger


# ==========================================
# SINGLE DRIVER FIXTURE (Chrome + Edge + Firefox)
# ==========================================
@pytest.fixture
def setup(request):
    browser = ConfigReader.get_browser().lower()
    request.browser = browser

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--allow-running-insecure-content")
        options.set_capability("acceptInsecureCerts", True)
        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.set_capability("acceptInsecureCerts", True)
        driver = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.accept_insecure_certs = True
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(ConfigReader.get_implicit_wait())
    driver.get(ConfigReader.get_base_url())

    yield driver
    driver.quit()


# ===============================
# LOGGER FIXTURE
# ===============================
@pytest.fixture
def logger(request):
    logger, log_file = get_logger(request.node.name)
    request.node.log_file = log_file
    return logger


# =====================================================================
# HTML REPORT ENHANCEMENT + SCREENSHOT ON FAILURE + LOG ATTACHMENT
# =====================================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        # ---------- 1️⃣ Attach execution logs ----------
        log_file = getattr(item, "log_file", None)
        if log_file and os.path.exists(log_file):
            with open(log_file, "r") as f:
                log_content = f.read()
            if log_content:
                report.sections.append(("Execution Logs", log_content))

        # ---------- 2️⃣ Screenshot on failure ----------
        if report.failed:
            driver = item.funcargs.get("setup")
            browser = getattr(item, "browser", "unknown_browser")

            if driver:
                screenshots_dir = item.config.screenshots_dir

                import re
                error_msg = str(report.longrepr).split("\n")[-1][:50]
                error_msg = re.sub(r"[^\w\-_.]", "_", error_msg)

                timestamp = datetime.now().strftime("%H-%M-%S")

                screenshot_file = (
                    f"{item.name}_{error_msg}_{browser}_{timestamp}.png"
                )

                screenshot_path = os.path.join(screenshots_dir, screenshot_file)

                driver.save_screenshot(screenshot_path)

                report.sections.append(
                    ("📸 Failure Screenshot", f"Saved to: {screenshot_path}")
                )

                print(f"\n[✔] Screenshot captured: {screenshot_path}")


# ==========================================
# AUTO TIMESTAMPED HTML REPORT + FOLDERS
# ==========================================
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    browser = ConfigReader.get_browser().lower()

    run_dir = os.path.join("reports", f"{browser}_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)

    screenshots_dir = os.path.join(run_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    config.run_dir = run_dir
    config.screenshots_dir = screenshots_dir

    if not config.option.htmlpath:
        html_report_path = os.path.join(
            run_dir, f"report_{browser}_{timestamp}.html"
        )
        config.option.htmlpath = html_report_path

        print(f"[+] HTML report will be generated at: {html_report_path}")