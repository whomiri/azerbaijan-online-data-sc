import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from deep_translator import GoogleTranslator

# Add ChromeDriver path here
chrome_driver_path = '/usr/local/bin/chromedriver'  # Example: '/usr/local/bin/chromedriver'

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # To run the browser in the background

# Start webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def search_name(name):
    # Opening
    driver.get('https://exidmet.justice.gov.az:8284/VVA/Names')
    
    # Find the name search box and type the name
    search_box = driver.find_element(By.ID, 'txtName')
    search_box.send_keys(name)
    
    # Press the search button
    search_button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'searchWithParams')]")
    search_button.click()
    
    # Wait 2 seconds for results to load
    time.sleep(2)

    # Get results
    try:
        results_table = driver.find_element(By.ID, 'tblData')
        results_text = results_table.text  # Get results
        return results_text.splitlines()  # Make each row a separate list element
    except Exception as e:
        return f"Sonuçlar alınamadı: {e}"

def filter_results(results, keyword):
    filtered = [result for result in results if keyword in result]
    return filtered

if __name__ == '__main__':
    name_to_search = input("Azerbaycan adını girin: ")
    results = search_name(name_to_search)

    # Get language preference from user
    lang_choice = input("Language? (1: Azerbaycan dili, 2: English Language): ")

    # Filter results
    filtered_results = filter_results(results, name_to_search)

    if lang_choice == '2':
        translated_results = [GoogleTranslator(source='az', target='en').translate(result) for result in filtered_results]
        print("Results:")
        for res in translated_results:
            print(res)
    else:
        print("Nəticə:")
        for res in filtered_results:
            print(res)

    # Close browser
    driver.quit()
