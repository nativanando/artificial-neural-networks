from yahoo_finance import Share
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import subprocess


yahoo = Share('AAPL')
print (yahoo.get_open())
print (yahoo.get_price())
print (yahoo.get_trade_datetime())

yahoo.refresh()
print ('refresh')
print (yahoo.get_price())

dadosHistoricos = yahoo.get_historical('2017-02-01' , '2017-05-29')
pprint (dadosHistoricos.__len__())


def getDadosHistoricos():
    pprint(dadosHistoricos)
    print ('teste')

def plotaGrafico(data1, data2):
    x = 10 * np.array(range(len(data1)))
    plt.plot(x, data1, 'go')  # green bolinha
    plt.plot(x, data1, 'k:', color='orange')  # linha pontilha orange
    plt.plot(x, data2, 'r^')  # red triangulo
    plt.plot(x, data2, 'k--', color='blue')  # linha tracejada azul
    plt.axis([0, 50, 0, 11])
    plt.title("Mais incrementado")
    plt.grid(True)
    plt.xlabel("eixo horizontal")
    plt.ylabel("que legal")
    plt.show()
    plt.savefig("test.png")
    return_code = subprocess.call('gimp test.png', shell=True)

data1 = [10, 5, 2, 4, 6, 8]
data2 = [1, 2, 4, 8, 7, 4]
getDadosHistoricos()
plotaGrafico(data1, data2)



