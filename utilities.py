import csv

def new_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names):
    
    with open(file_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for i in range(len(articles)):
                # row = {'article_name': articles[i], 'price': prices[i], 'link': links[i], 'date': just_date}
                # row = {'article_name': articles[i], 'price': prices[i], 'odo': odos[i], 'year': years[i], 'location': locations[i], 'link': links[i], 'date': just_date}
                row = {'article_name': articles[i], 'price': prices[i], 'odo': odos[i], 'year': years[i], 'location': locations[i], 'date': just_date, 'link': links[i] }
                writer.writerow(row)


def update_csv(file_csv, articles, prices, odos, years, locations, links, just_date, field_names):

    with open(file_csv, 'a+', newline='') as write_obj:
        csv_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        # Add contents of list as last row in the csv file
        for i in range(len(articles)):
            # row = {'article_name': articles[i], 'price': prices[i], 'odos': odos[i], 'years': years[i], 'location': locations[i], 'link': links[i], 'date': just_date}
            # row = {'article_name': articles[i], 'price': prices[i], 'odo': odos[i], 'year': years[i], 'location': locations[i], 'link': links[i], 'date': just_date}
            row = {'article_name': articles[i], 'price': prices[i], 'odo': odos[i], 'year': years[i], 'location': locations[i], 'date': just_date,'link': links[i]}
            csv_writer.writerow(row)  


def verify_file(content_folder, file_csv):
    for item in content_folder:
        if item == file_csv:
            return True
        else:
            pass
        
    return False

def main(tipoBot):
    file_csv = input("Sobre que archivo quieres escribir los resultados: ")
    URL = 'https:www.mercadolibre.com'
    car_bot = tipoBot(URL)
    array_search = (['nissan sentra', 'kia vibro', 'kia sportage', 'mazda 3',
     'toyota corolla', 'volkswagen jetta', 'nissan qashqai'])
    for car in array_search:
        car_bot.search_car(car, file_csv)
    # car_bot.real_change_page()
    car_bot.tearDown()