from webdriver_singleton import WebDriverSingleton
from home_page import HomePage
from search_result import SearchResult
import pytest
import json
from check_filter import CheckSorting
from config_reader import ConfigReader
from test_data_reader import TestDataReader


@pytest.fixture(scope="function")
def driver():
    driver_instance = WebDriverSingleton()
    driver_instance.driver.maximize_window()
    yield driver_instance.driver
    driver_instance.clear()


@pytest.mark.parametrize(
    "game, n",
    [(game['game'], game['n']) for game in TestDataReader.test_data['steam_games']]
)
def test_steam(driver, game, n):
    test_results = []
    cfg = ConfigReader()
    home = HomePage(driver)
    driver.get(cfg.return_value("STEAM_LINK"))
    assert home.is_page_opened(), 'Expected result: Home page was opened\n Actual result:Home page was not opened'
    driver.maximize_window()
    home.enter_game(game)
    home.click_search()
    search_page = SearchResult(driver)
    assert search_page.is_search_page_opened(
        game), 'Expected result:Search result page was opened\n Actual result:Search result page was not opened'
    search_page.use_filter()
    games = search_page.get_data(n)
    test_results.append(games)
    print(test_results)
    cfilter = CheckSorting()
    assert cfilter.is_sorting_working(
        games), 'Expected result:Sorting applied successfully\n Actual result:Sorting didn`t work'
