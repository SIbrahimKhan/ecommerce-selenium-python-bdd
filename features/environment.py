import os
from datetime import datetime

from behave import register_type
import parse

from utils.driver_factory import DriverFactory
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")

#so the test can take empty value in text field for -ve scenarios
@parse.with_pattern(r".*")
def parse_maybe_empty(text):
    return text
register_type(MaybeEmpty=parse_maybe_empty)

def before_all(context):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def before_scenario(context, scenario):
    context.driver = DriverFactory.get_driver()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        _attach_screenshot(context, scenario)
    if getattr(context, "driver", None):
        context.driver.quit()

def _attach_screenshot(context, scenario):
    timestamp = datetime.now().strftime("%D%M%Y_%H%M%S")
    ss_name = "".join(c if c.isalnum() else "_" for c in scenario.name)[:60]
    filename = f"{ss_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    try:
        context.driver.save_screenshot(filepath)
        print(f"[failed screenshot] saved to {filepath}")
        try:
            import allure
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except ImportError:
            pass

    except Exception as e:
        print(f"could not capture screenshot: {e}") 