from selenium import webdriver
from time import sleep as s
from selenium.webdriver.common.keys import Keys

async def main():
    PATH = 'webdriver/chromedriver.exe'

    driver = webdriver.Chrome(PATH)

    driver.get('https://randomicle.com/')

    s(0.5)

    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/button').click()

    s(1)

    url = driver.find_element_by_class_name("ImageLink").get_attribute('href')

    driver.quit()

    return url

