from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants import *
import pytest
class Test_Kodlamaio:
    # setup_method => pytest'te her test öncesi çalıştırılan metot
    # driver oluşturma
    def setup_method(self):
        # buradaki kodlar her test öncesi çalışır..
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # klasör oluşturma
        self.today = str(date.today())
        Path(self.today).mkdir(exist_ok=True) # make directory

    # teardown_method => her test sonrası çalışır..
    def teardown_method(self):
        # buradaki kodlar her test sonrası çalışır..
        self.driver.quit()

    # class fonksiyonlarının ilk parametresi her zaman "self"'dir
    def test_login(self):
        # assert => verilen conditionu testin sonucuna bağlar
        # text == "merhaba"
        self.driver.get(BASE_DOMAIN_URL)
        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath))) # defansif kodlama
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtnText = loginBtn.text
        self.driver.save_screenshot(self.today+"/test-login.png")
        #constant => SABİT değişkenler. Pİ sayısı
        assert loginBtnText == LOGIN_TEXT

    @pytest.mark.skip # ilgili testin testler koşulurken es geçilmesini sağlar.
    def test_register(self):
        self.driver.get(BASE_DOMAIN_URL)
        assert "Giriş Yap" == LOGIN_TEXT
#annotation-decorator

