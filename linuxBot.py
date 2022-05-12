from libraries import * 

class linuxBot(linuxHeadless):

    def __init__(self, URL, DP, DL, BL, UA):
        linuxHeadless.__init__(self, URL, DP, DL, BL, UA)

    def search_car(self, search, file_csv, LINUX_PATH):
        linuxHeadless.search_car(self, search, file_csv, LINUX_PATH)

    def tearDown(self):
        linuxHeadless.tearDown(self)

def main():
    # file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    file_csv = 'final_cars.csv'
    URL = 'https:www.mercadolibre.com'
    LINUX_PATH = '/home/ubuntu/carBotClean'
    DP = "/home/ubuntu/scraper/Last_files"
    DL = "/usr/bin/chromedriver"
    BL = "/usr/bin/google-chrome"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    car_bot = linuxBot(URL, DP, DL, BL, UA)
    search_array = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volvo', 'audi a4', 'audi a5', 'audi a6', 'volkswagen jetta', 'nissan qashqai', 'bmw serie 3', 'bmw serie 4', 'bmw serie 5', 'bmw serie m'])
    for car in search_array:
        car_bot.search_car(car, file_csv, LINUX_PATH)
    car_bot.tearDown()

if __name__ == '__main__':
    main()