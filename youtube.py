from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

video_url = "https://www.youtube.com/watch?v=coYCbroyq-s"

chrome_options = Options()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_service = Service("/usr/lib/chromium-browser/chromedriver")

driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
wait = WebDriverWait(driver, 10)
driver.get(video_url)
ActionChains(driver).move_to_element(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ytp-chrome-controls")))).perform()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.ytp-fullscreen-button.ytp-button"))).click()

while True:
    continue
