
from selenium import webdriver

# specify the path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path='chromedriver')

# navigate to a webpage
driver.get("http://127.0.0.1:5000/")

# find the element with id "score"
score_element = driver.find_element_by_id("score")

# extract the text value of the element
score_text = score_element.text

# convert the text to an integer
score = int(score_text)

print(score)

# close the browser
driver.quit()
