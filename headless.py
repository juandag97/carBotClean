from selenium import webdriver
from time import sleep
import datetime 
import csv
import os
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from utilities import verify_file, update_csv, new_csv

class windowsHeadless():

    def __init__(self, URL):
        # PATH = "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get(URL)
        driver.implicitly_wait(30) 
        driver.maximize_window() 

    def headlessInit(self, URL, DP, DL, BL, UA):
        download_path = DP
        driver_location = DL
        binary_location = BL
        user_agent = UA
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

    def search_car(self, search, file_csv, OUT_PATH):
        driver = self.driver 
        driver.get('https:www.mercadolibre.com')
        driver.find_element_by_id('CO').click()
        # country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys(search)
        search_field.submit()
        sleep(3)

        order_menu = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > button')
        order_menu.click()
        #lower_price = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(2)')
        higher_price = driver.find_element_by_xpath('/html/body/main/div/div/section/div[1]/div/div/div/div[2]/div/div/div/div/ul/li[3]')
        # lower_price.click()
        higher_price.click()
        sleep(3)

        articles, prices, odos, locations, years, links = [], [], [], [], [], []
        for j in range(0, 11):
            for i in range(3):
                try:
                #article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[1]/li[{i + 1}]/div/div/a/div/div[3]/h2').text
                    # article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[3]/h2').text
                    article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[3]/h2').text
                    articles.append(article_name)
                    # article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[1]/div/div/span/span[2]').text 
                    # article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[1]/div/div/span/span[2]/span[2]').text
                    article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[1]/div/div/div/span/span[2]/span[2]').text
                    prices.append(article_price)
                    article_element = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a')
                    article_link = article_element.get_attribute('href')
                    links.append(article_link)
                    article_odo = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[2]/ul/li[2]').text
                    article_year = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[2]/ul/li[1]').text
                    article_location = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol[{j + 1}]/li[{i + 1}]/div/div/a/div/div[4]/span').text
                    odos.append(article_odo)
                    years.append(article_year)
                    locations.append(article_location)
                except NoSuchElementException:
                    break

        # return articles, prices, odos, locations, years, links
        # print(articles, prices, links)

        actual = datetime.datetime.now()
        just_date = actual.strftime("%Y-%m-%d %H:%M")

        field_names = ['article_name', 'price', 'odo', 'year', 'location', 'date', 'link']
        # content_folder = os.listdir('/home/jesus/Developer/bots/shopping')
        content_folder = os.listdir(OUT_PATH)
        # print(OUT_PATH)
        # content_folder = os.listdir('D:\\Actually\\Development\\Cleanbots')
        # update_csv(file_csv, articles, prices, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, links, just_date, field_names)
        update_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names)

    def tearDown(self):
        self.driver.quit()

class linuxHeadless(windowsHeadless):

    def __init__(self, URL, DP, DL, BL, UA):
        windowsHeadless.headlessInit(self, URL, DP, DL, BL, UA)        

    def search_car(self, search, file_csv, LINUX_PATH):
        windowsHeadless.search_car(self, search, file_csv, LINUX_PATH)
        
    def tearDown(self):
        self.driver.quit()