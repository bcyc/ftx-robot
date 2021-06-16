from ftx.client import FtxClient


LEND_COINS = ['ETH', 'USD']


def auto_lending(client: FtxClient) -> None:
    for coin in LEND_COINS:
        lend_coin(client, coin)


def lend_coin(client: FtxClient, coin: str) -> None:
    print('[lend_coin] DEBUG:')
    balance_coin = client.get_balance_coin(coin)
    if balance_coin is None:
        return
    available_balance = balance_coin['free']
    lend_rate = client.get_margin_lending_rate_coin(coin)
    print(lend_rate)

    if available_balance > 0:
        client.lends(coin=coin, size=available_balance, rate=lend_rate['estimate'])