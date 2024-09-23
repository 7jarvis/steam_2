from webdriver_singleton import WebDriverSingleton
from home_page import HomePage
from search_result import SearchResult
import pytest
import json
from home_page import ConfigReader
from check_filter import CheckFilter

with open('test_data.json', 'r') as f:
    test_data = json.load(f)


@pytest.fixture(scope="module")
def driver():
    driver_instance = WebDriverSingleton.get_instance()
    driver_instance.driver.maximize_window()
    yield driver_instance.driver
    driver_instance.quit()


@pytest.mark.parametrize(
    "game_data",
    test_data['steam_games']
)
def test_steam(driver, game_data):
    test_results = []
    game = game_data['game']
    n = game_data['n']
    cfg = ConfigReader()
    home = HomePage(driver)
    driver.get(cfg.STEAM_LINK)
    assert home.is_homepage_opened(), 'Home page was not opened'
    driver.maximize_window()
    home.enter_game(game)
    home.click_search()
    search_page = SearchResult(driver)
    assert search_page.is_search_page_opened(game), 'Search result page was not opened'
    search_page.use_filter()
    games = search_page.retrieve_data(n)
    test_results.append(games)
    print(test_results)
    cfilter = CheckFilter()
    assert cfilter.is_filtering_working(games), 'Filter didn`t work'
