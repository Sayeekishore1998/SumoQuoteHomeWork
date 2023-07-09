import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# ----------Chrome webdriver invoking-----------------------------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:/Users/santh/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(3)

# ---------getting the website-----------------------------------#

driver.get("https://sumoquoteweb-qa.azurewebsites.net/new-account")

driver.save_screenshot("browser.png")

# ---------Filling out all the fields----------------------------#

driver.find_element(By.XPATH, "//input[@id='accountName']").send_keys("HSS Solutions")  # Organization name
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Sayeekishore")  # FirstName
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Bojja")  # LastName

emailId = "sayeekishoretest1@gmail.com"
driver.find_element(By.CSS_SELECTOR, "#emailAddress").send_keys(emailId)  # EmailAddress
driver.find_element(By.XPATH, "//input[@id='phoneNumber']").send_keys("2269754579")  # PhoneNumber
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Password@123")  # PassWord
driver.find_element(By.XPATH, "//input[@id='repeatPassword']").send_keys("Password@123")  # ConfirmPassword




# ----------Dropdown logic--------------------------------------#



dropdown = driver.find_element(By.ID, "howHeard")
dropdown.click()
dropdown_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "howHeard")))

option = dropdown_menu.find_element(By.XPATH, "//div[@class='v-list-item__title'][normalize-space()='Google']")
option.click()

time.sleep(3)

# ----------------Selecting the Checkbox---------------#

checkbox = driver.find_element(By.XPATH, "//div[@class='v-input--selection-controls__ripple']")
if not checkbox.is_selected():
    checkbox.click()

# --------------Saving the details----------------------#

save = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
save.click()

driver.save_screenshot("sumoquote3.png")

