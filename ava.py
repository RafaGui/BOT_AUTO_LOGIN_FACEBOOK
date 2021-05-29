from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time as s

cad = list()
login = str(input('Digite seu login: '))
passw = str(input('Digite sua senha: '))

cad.append(passw)
cad.append(login)

drive = webdriver.Chrome(ChromeDriverManager().install())
drive.get("https://www.facebook.com")
drive.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(login)
s.sleep(3)
drive.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(passw)
drive.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').send_keys(Keys.ENTER)

print(cad)