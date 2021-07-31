from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


#open chrome
driver = webdriver.Chrome(
    executable_path=r'C:/Users/Ajay/Downloads/chhrome-driver/chromedriver.exe')

#open URL
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeVDgMbWcdbtpcAnjGBt3avEu4RkmV8dU5hl10_zVs-z3hhRg/viewform')

time.sleep(2)

name = "Ajay"
#copy xpath from inspect>element>copy>copy xpath
text = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
)

text.send_keys(name)

# domain_select = Select(driver.find_element_by_name('Domain'))
# domain_select.select_by_visible_text('Tech')

dropDown = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
)
dropDown.click()

tech = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/span'
)
tech.click()

# submit = driver.find_element_by_xpath(
#     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
# submit.click()
