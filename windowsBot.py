from libraries import *

class windowsBot(windowsHeadless):

    def __init__(self, URL):
        windowsHeadless.__init__(self, URL)
        

    def search_car(self, search, file_csv, OUT_PATH):
        windowsHeadless.search_car(self, search, file_csv, OUT_PATH)

    def tearDown(self):
        windowsHeadless.tearDown(self)

def main():
    file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    OUT_PATH = 'D:\\Actually\\Development\\Cleanbots'
    URL = 'https:www.mercadolibre.com'
    car_bot = windowsBot(URL)
    search_array = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volvo', 'audi a4', 'audi a5', 'audi a6', 'volkswagen jetta', 'nissan qashqai', 'bmw serie 3', 'bmw serie 4', 'bmw serie 5', 'bmw serie m'])
    for car in search_array:
        car_bot.search_car(car, file_csv, OUT_PATH)
    car_bot.tearDown()

if __name__ == '__main__':
    main()