print('***************************************\nMy Coffee and Muffin Shop')
#Write a program that asks user for number of coffee and muffins being purchased
#Then have the user input values then have it display a response prompt
coffeePurchased = int(input("Number of Coffee's bought?\n"))
muffinsPurchased = int(input("Number of Muffins bought?\n"))
print('***************************************\n\n***************************************')
print('My Coffee and Muffin Shop Receipt')
Coffee = int(5)
Muffin = int(4)
cof = Coffee * coffeePurchased
muf = Muffin * muffinsPurchased
import decimal
from decimal import Decimal
x = Decimal('0.00')
tax = (float(cof + muf) * .06)
total = cof + muf + tax
print(coffeePurchased,"Coffee at $",Coffee,'each: $',cof)
print(muffinsPurchased,"Muffins at $",Muffin,'each: $',muf)
print('6% tax: $',tax)
print('---------')
print('Total: $',total)
print('***************************************')
