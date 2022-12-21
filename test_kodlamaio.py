from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
class Test_Kodlamaio:
    # class fonksiyonlarının ilk parametresi her zaman "self"'dir
    def test_login(self):
        # assert => verilen conditionu testin sonucuna bağlar
        # text == "merhaba"
        driver = webdriver.Chrome()
        driver.get("https://www.kodlama.io/")
        loginBtnXPath = "//*[@id='navbar']/div/div/div/ul/li[3]/a"
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath))) # defansif kodlama
        loginBtn = driver.find_element(By.XPATH,loginBtnXPath)
        loginBtnText = loginBtn.text
        assert loginBtnText == "Giriş Yap"
    