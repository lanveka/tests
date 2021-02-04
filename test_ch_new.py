import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск  при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_2020(self) :
        driver = self.driver
        # открытие  страницы http://www.python.org/psf-landing/

        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "2020 in Review"
        elem = driver.find_element_by_link_text("2020 in Review")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)



    def test_applications(self) :
        driver = self.driver
        # открытие страницы http://www.python.org/psf-landing/

        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "Applications"
        elem = driver.find_element_by_link_text("Applications")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)


    def test_news(self) :
        driver = self.driver
        driver.get("http://www.python.org")
        # получаем список ссылок в меню News по CSS-селектору
        elems = driver.find_elements_by_css_selector('#news li a')
        href_list = []
        name_list = []
        for e in elems :
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))
        for i in range(len(href_list)-1):
            # переходим по ссылкам
            driver.get(
                href_list[i]
            )
            
            time.sleep(3)

if __name__ == '__main__' :
    unittest.main()
