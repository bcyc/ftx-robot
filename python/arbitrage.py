from ftx.client import FtxClient
import datetime
from traceback import format_exc

def spot_futures_arbitrage(coin: str) -> None:
    print('[spot_futures_arbitrage] DEBUG: {}'.format(datetime.datetime.now()))
    # 取得 USD_balance
    # 計算 batch = 15 / price .2f
    # Open if USD_balance >= 15 and leverage < 3
    # Close if spot & future > batch and leverage > 4

    # Open
    #   BUY batch spot & SELL batch future
    # Close
    #   SELL batch spot & BUY batch future

def open_arbitrage(client: FtxClient, coin: str, spotSize: float, futureSize: float) -> None:
    print('[open_arbitrage] DEBUG: {}'.format(datetime.datetime.now()))
    print('[open_arbitrage] DEBUG: coin = {}, spotSize = {}, futureSize= {}'.format(coin, spotSize, futureSize))

def close_arbitrage(client: FtxClient, coin: str, spotSize: float, futureSize: float) -> None:
    print('[close_arbitrage] DEBUG: {}'.format(datetime.datetime.now()))
    print('[close_arbitrage] DEBUG: coin = {}, spotSize = {}, futureSize= {}'.format(coin, spotSize, futureSize))