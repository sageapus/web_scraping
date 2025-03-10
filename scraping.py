from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

url = "https://www.mrphome.com/en_za/search?q=vase"
driver.get(url)
wait = WebDriverWait(driver, 10)


# XPath with 'contains' for multiple classes
products= driver.find_elements(By.CSS_SELECTOR, ".product.listing-page")

for product in products:
    name=product.find_element(By.XPATH,'.//ion-text').text
    price=product.find_element(By.XPATH,'.//ion-label').text
    print(price,name)
# class="product-grid md"
# class="product listing-page size-6 size-3-md size-3-lg md"

# //*[@id="main-content"]/div/div[2]/div/ion-grid[1]/ion-row/ion-col[1]/ion-list/ion-label