from selenium import webdriver
driver = webdriver.Chrome('chromedriver')


def test_scores_service():
    driver.get("http://3.125.145.138:8777/")
    score_element = int(driver.find_element_by_id("score").text)
    if 1000 >= score_element >= 1:
        return True
    else:
        return False


def main_function():
    # The main function will return -1 as an OS exit
    # code if the tests failed and 0 if they passed.
    test = test_scores_service()
    if test:
        return 0
    else:
        return -1


main_function()
