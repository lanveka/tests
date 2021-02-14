import unittest
from selenium import webdriver
import time
import os
# в именах сохраненных файлов ставится дата
import datetime
# класс для обработки PDF
import textract
# для очистки папки с сохраненными файлами после теста
import shutil
import time

class LogTestCase(unittest.TestCase):
    # подготовка к каждому тесту
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()
        self.driver.get('https://shop.cravt.by/')
        time.sleep(5)
    def test_catalog(self) :
        driver = self.driver
        elem = driver.find_element_by_xpath('//*[@id="root"]/header/div[2]/div/div/div[1]/div[2]/div/form/input[1]')
        elem.click()
        elem.send_keys("Туалетная вода Moschino FUNNY!")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath('//*[@id="root"]/header/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/a')
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath('//*[@id="root"]/main/div[4]/div/div/div/div[2]/div/div/div/a')
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_css_selector('#root > main > div.catalog-item-block > div > div > div > div.catalog-item__offers-list > div > div:nth-child(2) > div > div.product__action.flc > div > div > div.basket-action__cell-btn > button > span')
        elem.click()
        time.sleep(5)

if __name__ == '__main__' :
    unittest.main()
