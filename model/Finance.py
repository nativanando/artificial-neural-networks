from yahoo_finance import Share
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import subprocess

yahoo = Share('YHOO')
print(yahoo.get_open())
print(yahoo.get_price())
print(yahoo.get_trade_datetime())

yahoo.refresh()
print('refresh')
print(yahoo.get_price())


dadosHistoricos = yahoo.get_historical('2017-06-06', '2017-06-06')

pprint(dadosHistoricos.__len__())


def getDadosHistoricos():
    pprint (dadosHistoricos)
    print('teste')

getDadosHistoricos()

