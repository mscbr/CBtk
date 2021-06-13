import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexFuturesClient

from decouple import config

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient(True, config("APIKEY_PUBLIC_BINANCE_TESTNET"),
                                   config("APIKEY_PRIVATE_BINANCE_TESTNET"))
    bitmex = BitmexFuturesClient(
        True, config("APIKEY_PUBLIC_BITMEX_TESTNET"),
        config("APIKEY_PRIVATE_BITMEX_TESTNET"))

    root = tk.Tk()
    root.mainloop()
