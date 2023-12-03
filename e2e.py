from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

def test_scores_service():
    url = input("URL: ")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver_path = Service(r'C:\Users\amits\OneDrive\שולחן העבודה\DEVOPS - EXPERTS/chromedriver.exe')
    driver = webdriver.Chrome(service=driver_path, options=chrome_options)

    driver.get(url)
    element = str(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//p'))).text)
    if 'Error' in element:
        return False
    else:
        element_score = int(str(element).split(':')[1].strip())
        if 1<element_score<1000:
            return True

    driver.quit()

def main_function():
    return -1 if not test_scores_service() else 0
