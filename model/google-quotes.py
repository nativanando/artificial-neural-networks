import pandas_datareader.data as web
import datetime
import json
from pprint import pprint

start = datetime.datetime(2001, 1, 1)

end = datetime.datetime(2017, 1, 27)

f = web.DataReader("fb", 'google', start, end)
f.to_csv('/home/fernando/Documentos/TCC/teste.csv')