from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Opera()# указываем с каким браузером будем работать

driver.get('https://www.sis.gov.uk/#maincontent.html')# вводим URL нашего сайта

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]"))).click()

promo = driver.find_element_by_xpath('/html/body/main/section[1]/div[4]/a') #захватываем элемент на странице
promo.click()# кликаем по данному элементу

time.sleep(5)# делаем паузу в 5 секунд для того чтобы ролик прогрузился

driver.save_screenshot('C:/Users/Arcana Mace/Desktop/save_screenshot.png') #делаем скриншот и сохраняем его

time.sleep(3)# делаем паузу чтобы скриншот успел сохраниться


driver.quit()# закрываем браузер.