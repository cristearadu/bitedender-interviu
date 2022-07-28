from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages.home_screen_page import HomeScreenPage
from core_elements.pages.solutions_page import Solutions


@step("Navigate to home screen -> See solutions")
def navigate_to_see_solutions():
    home_screen = HomeScreenPage()
    home_screen.click_home_solutions_button()
    assert Driver.driver.check_exists(Solutions.MULTIPLATFORM), "Failed to load \'Solutions\' page"
