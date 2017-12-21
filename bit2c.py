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
URL = 'https://www.bit2c.co.il/Order/index'
CHROMEPATH = 'chromedriver'
PHANTOMPATH = 'phantomjs'
output = "bit2c_ILS.csv"

DEBAG=False

class App:

    def __init__(self):
        if (os.path.exists(output)):
	        print("*    The last output file will be overwriten? ")
        	print("*    that's the time to copy it's else where ")
        	input( "*         Press Enter To Confiram.")
        # load the last time
        self.newesttime=datetime(2009, 12, 2, 9, 30)
        self.browser=None
        if DEBAG:
            self.setup_chrome()
        else:
            self.setup_headless()
        self.random_sleep(3)
        self.browser.get(URL)

        with open(output,'w',encoding="utf-8") as self.writer:
                self.writeCsvOrder()
                while (True):
                    self.collect()
                    time.sleep(Timetowait)
                    self.browser.refresh();
                    print("***************")


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
        table = self.browser.find_element_by_css_selector("table[id='tblTradesHistory']")
        self.Toview(table)
        tabletext=table.text
        tabletext=tabletext.replace(",","")
        rows=tabletext.split("\n")
        rows.reverse()
        for i in range(0,len(rows)-4):
            row=rows[i].split(" ")
            dataTime=row[0]+" "+row[1]
            currentsample=datetime.strptime(dataTime, '%H:%M:%S %d/%m/%y')
            if (currentsample>self.newesttime):
                print("Inserted at "+dataTime)
                printable=dataTime+","+row[2]+","+row[3]+","+row[4]+"\n"
                self.write(printable)
                self.newesttime=currentsample


    def load_from_prev(self):
        with open(output,'r',encoding="utf-8") as reader:
            content = reader.readlines()
        for i in range(1,len(content)):
            data=content[i]
            newesttimec=datetime.strptime(data.split(",")[0], '%H:%M:%S %d/%m/%y')
            if (self.newesttime<newesttimec):
                self.newesttime=newesttimec

    def random_sleep(self,min_val):
        time_wait = min(MAX_RANDOM, max(min_val, random.gauss(MU, STD)))
        time.sleep(time_wait)



    def move_to_elm(self,element):
        action = webdriver.ActionChains(self.browser)
        action.move_to_element(element)
        action.perform()




    def writeCsvOrder(self):
        self.write("Data,Price In Shkel,BTC amount,total \n")
        self.writer.flush()

    def write(self,strs):
        self.writer.write(strs)
        self.writer.flush()

    def Toview(self,element):
       # self.browser.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.browser).move_to_element(element).perform()
        self.random_sleep(1)

App()
