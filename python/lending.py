from ftx.client import FtxClient
import datetime
from traceback import format_exc

LEND_COINS = ['ETH', 'USD']


def auto_lending(client: FtxClient) -> None:
    for coin in LEND_COINS:
        lend_coin(client, coin)


def lend_coin(client: FtxClient, coin: str) -> None:
    print('[lend_coin] DEBUG: {}'.format(datetime.datetime.now()))
    balance_coin = client.get_margin_lending_info_coin(coin)
    if balance_coin is None:
        return
    print(balance_coin)
    available_balance = float(format(balance_coin['lendable'], '.6f')) - 0.000001
    lend_rate = client.get_margin_lending_rate_coin(coin)
    print(lend_rate)

    if available_balance > 0:
        print('Lending coin: {}, size: {}, rate: {}'.format(coin, available_balance, lend_rate['estimate']))
        try:
            print(client.lends(coin=coin, size=available_balance, rate=lend_rate['estimate']))
        except:
            print(format_exc())