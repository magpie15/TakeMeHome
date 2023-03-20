# Creating the Web Driver -- using GeckoDriver because Firefox
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Launching the kayak German website in the Flights section:

url = "https://www.kayak.de/flights"
browser.get(url)
time.sleep(1)

# This should close any cookie pop-ups
accept_cookies_xpath = '/html/body/div[5]/div/div[3]/div/div/div[2]/div/div/div[1]/button'

try:
    browser.find_element(By.XPATH, accept_cookies_xpath).click()
except NoSuchElementException:
    pass


#From
from_click_xpath = ''
from_text_xpath = ''
departure_city = 'Munich'

browser.find_element(By.XPATH, from_click_xpath).click()
browser.find_element(By.XPATH, from_text_xpath).send_keys(Keys.BACKSPACE + Keys.BACKSPACE + departure_city)
time.sleep(0.5)

browser.find_element(By.XPATH, from_text_xpath).send_keys(Keys.Return)
time.sleep(1)

#To
to_click_xpath = ''
to_text_xpath = ''
arrival_city = 'Belize'

browser.find_element(By.XPATH, to_click_xpath).click()
browser.find_element(By.XPATH, to_text_xpath).send_keys(arrival_city)
time.sleep(0.5)

browser.find_element(By.XPATH, to_text_xpath).send_keys(Keys.RETURN)
time.sleep(1)