from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x = browser.find_element(By.ID, "input_value").text
    q = calc(int(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(q)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()