from bs4 import BeautifulSoup
import requests

while True:
    print('Wather')
    city = input('City? (Киев): ')
    if city == '':
        city = 'Киев'

    resp = requests.get(f'https://sinoptik.ua/погода-{city}/10-дней')

    soup = BeautifulSoup(resp.text, 'lxml')

    if soup.find("body", class_="ru p404"):
        print('404 Page Not Found')
    else:

        date_list = []
        date_dict = {}
        weather_list = (soup.find("div", class_="tabs").text).split()
        parser_city = (soup.find("div", class_="cityName").text).split()

        for i in range(0, len(weather_list), 7):
            n = weather_list[0 + i:7 + i]
            date_dict[n[1].lstrip('0')] = ' '.join(n)
            date_list.append(n[1].lstrip('0'))

        print(' '.join(parser_city))
        while True:
            input_date = input(f'Enter date from {date_list[0]} to {date_list[len(date_list) - 1]} : ')
            if input_date not in date_list:
                for i in date_dict.values():
                    print(i)
                break
            else:
                print(date_dict[input_date])
            if input('Choise another date? Y/n') != 'Y':
                break

    if input('Chise another city or exit? C/e') != 'C':
        break