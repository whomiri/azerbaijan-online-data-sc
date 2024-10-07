from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Specify ChromeDriver path
chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Specify your own ChromeDriver path

# Headless mode for Chrome (to run in the background)
options = Options()
options.add_argument("--headless")

#Start WebDriver service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open web page
driver.get("https://www.worldometers.info/world-population/azerbaijan-population/")

# Find class="rts-counter" and rel="azerbaijan-population" element
population_element = driver.find_element(By.CSS_SELECTOR, 'span.rts-counter[rel="azerbaijan-population"]')

# get population
population = population_element.text
print("Azerbaycan Əhalisi:", population)

# Close browser
driver.quit()
