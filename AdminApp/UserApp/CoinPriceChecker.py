from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def SupplyCoinData20():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '74d02b22-800a-4499-8f3a-b7a940a3003c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        coin_id = []
        coin_price = []

        for i in range(20):
            coin_id.append(data['data'][i]['symbol'])
            coin_price.append(data['data'][i]['quote']['USD']['price'])

        return coin_id, coin_price
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def SupplyCoinData2140():
    url = 'http://api.coinlayer.com/api/live?access_key=cb73e4d95e5509e722c6475ef2d9bf1d'

    import urllib.request
    with urllib.request.urlopen(url) as response:
        html = response.read()

    data = json.loads(html)

    coin_id = ["BTC", "ETH", "XRP", "BCH", "USDT", "LTC", "BNB", "EOS", "XLM", "TRX", "ADA", "XMR", "LEO", "DSH", "GNO", "DASH", "XLM"]
    coin_price = [data['rates']["BTC"], data['rates']["ETH"], data['rates']["XRP"], data['rates']["BCH"], data['rates']["USDT"],\
        data['rates']["LTC"], data['rates']["BNB"], data['rates']["EOS"], data['rates']["XLM"], data['rates']["TRX"],data['rates']["ADA"],\
            data['rates']["XMR"], data['rates']["LEO"], data['rates']["DSH"], data['rates']["GNO"], data['rates']["DASH"], data['rates']["XLM"]]

    return coin_id, coin_price 