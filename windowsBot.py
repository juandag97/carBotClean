from headless import windowsHeadless
from selenium import webdriver
from time import sleep
import datetime 
import csv
import os
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from utilities import verify_file, update_csv, new_csv

class windowsBot(windowsHeadless):

    def __init__(self, URL):
        # windowsHeadless.__init__(self, URL)
        PATH = "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe"
        # self.driver = webdriver.Chrome(executable_path = PATH) 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get(URL)
        driver.implicitly_wait(30) 
        driver.maximize_window() 

    def search_car(self, search, file_csv):
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

        # location = driver.find_element_by_partial_link_text('Bogotá D.C')
        # location.click()
        # sleep(3)

        # condition = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-filter-groups > dl:nth-child(7) > dd:nth-child(2) > a > span.ui-search-filter-name')
        # #condition.click()
        # driver.execute_script("arguments[0].click();", condition)
        # sleep(3)

        # order_menu = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button')
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
        content_folder = os.listdir('D:\\Actually\\Development\\bots\\headless')
        # update_csv(file_csv, articles, prices, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, links, just_date, field_names)
        update_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names)
         

    def change_page(self, array_search, file_csv):
        articles, prices, odos, locations, years, links = [], [], [], [], [], []
        temp_1, temp_2, temp_3, temp_4, temp_5, temp_6 = self.search_car(array_search, file_csv)
        articles.extend(temp_1)
        prices.extend(temp_2)
        odos.extend(temp_3)
        locations.extend(temp_4)
        years.extend(temp_5)
        links.extend(temp_6)
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/main/div/div/section/div[3]/ul/li[3]/a').click()
                temp_1, temp_2, temp_3, temp_4, temp_5, temp_6 = self.search_car(array_search[0], file_csv)
                articles.extend(temp_1)
                prices.extend(temp_2)
                odos.extend(temp_3)
                locations.extend(temp_4)
                years.extend(temp_5)
                links.extend(temp_6)
            except:
                try:
                    self.driver.find_element_by_xpath('/html/body/main/div/div/section/div[3]/ul/li[4]/a').click()
                    temp_1, temp_2, temp_3, temp_4, temp_5, temp_6 = self.search_car(array_search[0], file_csv)
                    articles.extend(temp_1)
                    prices.extend(temp_2)
                    odos.extend(temp_3)
                    locations.extend(temp_4)
                    years.extend(temp_5)
                    links.extend(temp_6)
                except:
                    actual = datetime.datetime.now()
                    just_date = actual.strftime("%Y-%m-%d %H:%M")

                    field_names = ['article_name', 'price', 'odo', 'year', 'location', 'date', 'link']
                    # content_folder = os.listdir('/home/jesus/Developer/bots/shopping')
                    content_folder = os.listdir('D:\\Actually\\Development\\bots\\headless')
                    # update_csv(file_csv, articles, prices, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, links, just_date, field_names)
                    update_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names) if verify_file(content_folder, file_csv) else new_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names)
                    break

    def real_change_page(self):
        driver = self.driver 

        driver.find_element_by_id('CO').click()
        # country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('nissan')
        search_field.submit()
        sleep(3)
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/main/div/div/section/div[3]/ul/li[3]/a').click()
                sleep(3)
            except:
                try:
                    self.driver.find_element_by_xpath('/html/body/main/div/div/section/div[3]/ul/li[4]/a').click()
                    sleep(3)
                except:
                    break

    def tearDown(self):
        self.driver.quit()
    


def main():
    file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    URL = 'https:www.mercadolibre.com'
    car_bot = windowsBot(URL)
    array_search = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volkswagen jetta', 'nissan qashqai'])
    for car in array_search:
        car_bot.search_car(car, file_csv)
    # car_bot.real_change_page()
    car_bot.tearDown()

if __name__ == '__main__':
    main()