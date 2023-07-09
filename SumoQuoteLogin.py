import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:/Users/santh/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)

driver.get("https://sumoquoteweb-qa.azurewebsites.net/signIn")



loginEmail = "sayeekishoretest1@gmail.com"
emailId = driver.find_element(By.CSS_SELECTOR, "input[placeholder='yours@example.com']")
emailId.send_keys(loginEmail)
passWord = driver.find_element(By.CSS_SELECTOR, "input[placeholder='your password']")
passWord.send_keys("Password@123")
logIn = driver.find_element(By.XPATH, "//span[@class='auth0-label-submit']")
logIn.click()


time.sleep(6)
getStarted = driver.find_element(By.XPATH, "//span[contains(text(),'Get started')]")
getStarted.click()

file_input = driver.find_element(By.XPATH, "//input[@type='file']")
image_path = "C:/Users/santh/Documents/sumo-web.png"
file_input.send_keys(image_path)


#colourSelect = driver.find_element(By.XPATH,
                # "//i[@class='v-icon notranslate far fa-exchange material-icons theme--light']")
#colourSelect.click()  # Primary to Secondary color

purpose = driver.find_element(By.XPATH, "//input[@id='capabilities']")
purpose.clear()
time.sleep(2)
purpose.send_keys("Roofing")

service = driver.find_element(By.XPATH, "//input[@id='capabilities2']")
service.clear()
time.sleep(2)
service.send_keys("Residential")


seeMyBrand_button = driver.find_element(By.CSS_SELECTOR,
                                        "button[class='btn-sumo-primary mt-8 v-btn v-btn--has-bg theme--light elevation-0 v-size--default'] span[class='v-btn__content']")
seeMyBrand_button.click()


confirmButton = driver.find_element(By.XPATH,
                                    "//button[@class='btn-sumo-primary mb-5 mt-0 v-btn v-btn--has-bg theme--light elevation-0 v-size--default']//span[@class='v-btn__content'][normalize-space()='Confirm']")
confirmButton.click()


typeOfWork = driver.find_element(By.XPATH, "//div[contains(text(),'Commercial Roofing')]")
typeOfWork.click()


time.sleep(3)

productLines_Ok = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]")
productLines_Ok.click()

finishButton = driver.find_element(By.XPATH, "//button[@class='btn-sumo-primary float-right v-btn v-btn--has-bg theme--light elevation-0 v-size--default']//span[@class='v-btn__content'][normalize-space()='Finish']")
finishButton.click()



LetsGo = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-sumo-primary v-btn v-btn--has-bg theme--light elevation-0 v-size--default'] span[class='v-btn__content']")
LetsGo.click()








