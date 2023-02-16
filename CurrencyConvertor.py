#install the module/package
#pip install forex-python

#import the module/package
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

test = CurrencyCodes()

cur_symbol = test.get_symbol('INR')
cur_name = test.get_currency_name('INR')

print("The currency name is ", cur_name)
print("The currency symbol is ", cur_symbol)

print("\n" + test.get_currency_name('USD'))
print(test.get_symbol('USD'))

test1 = CurrencyRates()

#convert dollar into rupees.
rate = test1.get_rate('USD','INR')
print("1 Dollar = " + str(rate) + " Rupees.")

#convert rupee into dollar.
rate = test1.get_rate('INR','USD')
print("1 Rupee = " + str(rate) + " Dollar.")

#convert 10 dollar into rupees.
res = test1.convert('USD','INR', 10)
print("10 Dollar = " + str(res) + " Rupees.")

print("###################################################")

bitcoin = BtcConverter()
price = bitcoin.get_latest_price('INR')

print("1 Bitcoin = " + str(price) + " Rupees.")




