from libraries import *

def main():
    file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    OUT_PATH = 'D:\\Actually\\Development\\Cleanbots'
    URL = 'https:www.mercadolibre.com'
    # download_path = "D:\\Actually\\Development\\bots\\headless"
    # driver_location = "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe"
    # binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    car_bot = windowsHeadless(URL)
    search_array = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volvo', 'audi a4', 'audi a5', 'audi a6', 'volkswagen jetta', 'nissan qashqai', 'bmw serie 3', 'bmw serie 4', 'bmw serie 5', 'bmw serie m'])
    for car in search_array:
        car_bot.search_car(car, file_csv, OUT_PATH)
    car_bot.tearDown()

if __name__ == '__main__':
    main()