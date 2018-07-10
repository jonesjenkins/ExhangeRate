import quandl
import pandas as pd
import matplotlib.pyplot as plt

exchange_rate = quandl.get('FED/RXI_N_B_JA', start_date='2017-3-3', end_date='2018-7-3')
df = pd.DataFrame(exchange_rate)
plt.title('JPY to USD Exchange Rate')
plt.xlabel('Day')
plt.ylabel('Yen to Dollar')
plt.plot(exchange_rate)
plt.show()