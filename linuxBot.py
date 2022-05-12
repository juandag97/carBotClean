from libraries import * 

class linuxBot(linuxHeadless):

    def __init__(self, URL):
        linuxHeadless.__init__(self, URL)

    def search_car(self, search, file_csv, LINUX_PATH):
        linuxHeadless.search_car(self, search, file_csv, LINUX_PATH)

    def tearDown(self):
        linuxHeadless.tearDown(self)

def main():
    file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    URL = 'https:www.mercadolibre.com'
    LINUX_PATH = '/home/jesus/Developer/bots/shopping'
    car_bot = linuxBot(URL)
    search_array = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volvo', 'audi a4', 'audi a5', 'audi a6', 'volkswagen jetta', 'nissan qashqai', 'bmw serie 3', 'bmw serie 4', 'bmw serie 5', 'bmw serie m'])
    for car in search_array:
        car_bot.search_car(car, file_csv, LINUX_PATH)
    car_bot.tearDown()

if __name__ == '__main__':
    main()