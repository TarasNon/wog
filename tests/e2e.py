from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome('tests\\chromedriver')



def test_scores_service():
    driver.get("http://127.0.0.1:5000")
    score_element = int(driver.find_element_by_id("score"))
    if 1000 >= score_element >= 1:
        return True
    else:
        return False



test_scores_service()
