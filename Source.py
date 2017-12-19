__author__ = 'tr1c4011'

import coinigy_api
import numpy as np

api = coinigy_api.CoinigyREST()

res = api.data("GDAX", "BTC/USD", "history")

arr_index = np.array(res['history'].price.index.time)
arr_value = np.array(res['history'].price.values)
arr_matrix = np.r_[arr_index[None,:],arr_value[None,:]]

arr_value_min = np.amin(arr_value)
arr_value_max = np.amax(arr_value)
"""
arr_index içerisindeki, datalardan ayn? time içerenlerde en yüksek olan?n seçilmesi ve bunun filtrelenmesi gerekiyor.
"""

import matplotlib.pyplot as plt

plt.plot(arr_index, arr_value, '-o')
plt.axis([np.amin(arr_index), np.amax(arr_index), arr_value_min, arr_value_max])
plt.show()

print(arr_matrix)