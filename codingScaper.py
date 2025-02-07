from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Automatically installs the correct ChromeDriver
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
# Open CodeChef profile
browser.get('https://www.codechef.com/users/vahsir7')
# Get the user's rating
rating = browser.find_element(By.CLASS_NAME, 'rating-number').text
print('Rating:', rating)
browser.quit()
