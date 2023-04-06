import requests
from bs4 import BeautifulSoup
headers = {"User-Agent" : 'Mozilla/5.0'}

def get_course():
    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=VES&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    vef_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=CUP&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    cup_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=VND&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    vnd_rub = div[:div.find('.') + 5]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=THB&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    thb_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=AED&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    aed_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EGP&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    egp_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=TRY&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    try_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    eur_rub = div[:div.find('.') + 3]

    base_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB'
    Get = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(Get.text, 'lxml')
    div = (soup.find('p', {'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})).text
    usd_rub = div[:div.find('.') + 3]
    # data = []
    # # Get THB/USD rate from Xe
    # with open('currency.txt') as f:
    #     for line in f.readlines():
    #         data.append(line)
    # thb_rub = data[0]
    # usd_rub = data[1]
    # eur_rub = data[2]
    # try_rub = data[3]
    # egp_rub = data[4]
    # aed_rub = data[5]
    # vef_rub = data[6]
    # cup_rub = data[7]
    # vnd_rub = data[8]



    return thb_rub, usd_rub, eur_rub, try_rub, egp_rub, aed_rub, vef_rub, cup_rub, vnd_rub

