from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('tests/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('http://3.125.145.138:8777')



score_element = int(driver.find_element_by_id("score"))
if 1000 >= score_element >= 1:
    print("Test OK!")
else:
    print("Test BAD")



# def main_function():
#     test = test_scores_service()
#     if test:
#         return 0
#     else:
#         return -1


# main_function()
