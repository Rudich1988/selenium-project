import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

s = Service('C:\\Users\\user\\Desktop\\c.py\\chromedriver')
opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=opt)
driver.maximize_window()
driver.get('https://www.avito.ru/')
aaa = 'https://www.avito.ru/'
input_tab = driver.find_element(By.CSS_SELECTOR, '#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-header-kdkEW.index-stickyHeader-WbpLL > div > div.index-search-xHvcz > div.index-form-ENoC5 > div.index-suggest-zkzTd > div > div > div > label.input-layout-input-layout-_HVr_.input-layout-size-s-COZ10.input-layout-text-align-left-U2OZJ.width-width-12-_MkqF.suggest-input-X6pqt.js-react-suggest > input')
input_tab.send_keys('ford')
driver.find_element(By.XPATH, '//span[@class="desktop-9uhrzn"]').click()
driver.find_element(By.XPATH, '//a[@title="Mondeo"]').click()

all_cars = []
for i in range(2):
    soup = bs(driver.page_source, 'lxml')
    cars = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
    for car in cars:
        name = car.find('div', 'iva-item-title-py3i_').a['title']
        link = 'https://www.avito.ru/' + car.find('div', 'iva-item-title-py3i_').a['href']
        all_cars.append(f'{name}: {link}')
    driver.find_element(By.XPATH, '//a[@data-marker="pagination-button/nextPage"]').click()
    time.sleep(10)

for count in range(len(all_cars)):
    print(all_cars[count])
