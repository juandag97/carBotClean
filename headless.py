from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import sleep
# import datetime
# import csv
# import os
# import sys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class windowsHeadless():

    def __init__(self, URL):
        download_path = "D:\\Actually\\Development\\bots\\headless"
        driver_location = "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe"
        binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option("prefs", {
            "download.default_directory": f"{download_path}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "safebrowsing.enabled": True
            })
        options.binary_location = binary_location
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument('--headless')
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options = options)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(15)
        self.driver.get(URL) 

class linuxHeadless():

    def __init__(self, URL):
    

        download_path = "/home/ubuntu/scraper/Last_files"
        driver_location = "/usr/bin/chromedriver"
        binary_location = "/usr/bin/google-chrome"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option("prefs", {
            "download.default_directory": f"{download_path}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "safebrowsing.enabled": True
            })
        options.binary_location = binary_location
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument('--headless')
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        # self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options = options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(15)
        self.driver.get(URL)