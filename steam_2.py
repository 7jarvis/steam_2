from webdriver_singleton import WebDriverSingleton
from home_page import HomePage
from search_result import SearchResult
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

TIMEOUT = 10
test_results = []


@pytest.fixture(scope="module")
def driver():
    driver = WebDriverSingleton.get_instance()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "game",
    [
        "The Witcher",
        "Fallout"
    ]
)
def test_steam(driver, game):
    home = HomePage(driver)
    home.open_page(home.STEAM_LINK)
    install_button = WebDriverWait(driver, TIMEOUT).until(
        ec.element_to_be_clickable(home.INSTALL))
    assert install_button, 'Home page was not opened'
    driver.maximize_window()
    home.enter_game(game)
    home.click_search()
    search_page = SearchResult(driver, game)
    tag = WebDriverWait(driver, TIMEOUT).until(
        ec.presence_of_element_located(search_page.searched))
    assert tag, 'Search result page was not opened'
    search_page.use_filter()
    n = 10 if game == "The Witcher" else 20
    games, prices = (search_page.retrieve_data(n))
    test_results.append(games)
    assert search_page.is_filtering_working(prices), 'Filter didn`t work'


