from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time,os
from datetime import datetime

import time
import random


import os
MU=5
STD=2
MAX_RANDOM=10
Timetowait=60
URL = 'https://il.investing.com/currencies/btc-usd'
CHROMEPATH = 'chromedriver'
PHANTOMPATH = 'phantomjs'
output = "investing_USD.csv"
DEBAG=False

class App:

    def __init__(self):
        if (os.path.exists(output)):
	        print("*    The last output file will be overwriten? ")
        	print("*    that's the time to copy it's else where ")
        	input( "*         Press Enter To Confiram.")
        self.browser=None
        if DEBAG:
            self.setup_chrome()
        else:
            self.setup_headless()
        self.browser.get(URL)
        with open(output,'w',encoding="utf-8") as self.writer:
                self.writeCsvOrder()
                while (True):
                    self.collect()
                    time.sleep(Timetowait)
                    #self.browser.refresh(); the site auto refresh
                    #print("***************")


    def chrome_prep(self):
       # get rid of asking to save password and notifications popup
        chrome_options = webdriver.ChromeOptions()

        chrome_options.EnablePersistentHover=False
        chrome_options.add_experimental_option(
            'prefs', {
                'credentials_enable_service': False,
                "profile.default_content_setting_values.notifications": 2,
                'profile': {
                    'password_manager_enabled': False
                }
            }
        )
        return chrome_options

    def setup_chrome(self):
        options = self.chrome_prep()
        os.environ["webdriver.chrome.driver"] = CHROMEPATH
        self.browser = webdriver.Chrome(CHROMEPATH, chrome_options=options)
        self.browser.set_window_position(0, 0)
        self.random_sleep(3)

    def setup_headless(self):
        self.browser = webdriver.PhantomJS(PHANTOMPATH)
        self.random_sleep(3)


    def collect(self):
        try:
            self.browser.switch_to_alert()
        except NoAlertPresentException:
            return False

        one = self.browser.find_element_by_css_selector("span[id='last_last']")
        current=one.text
        current=current.replace(",","")
        self.write(str(datetime.now())+","+current+"\n")



    def random_sleep(self,min_val):
        time_wait = min(MAX_RANDOM, max(min_val, random.gauss(MU, STD)))
        time.sleep(time_wait)



    def move_to_elm(self,element):
        action = webdriver.ActionChains(self.browser)
        action.move_to_element(element)
        action.perform()




    def writeCsvOrder(self):
        self.write("Date,Price In USD \n")
        self.writer.flush()

    def write(self,strs):
        self.writer.write(strs)
        self.writer.flush()

    def Toview(self,element):
       # self.browser.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.browser).move_to_element(element).perform()
        self.random_sleep(1)

App()
