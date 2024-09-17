print('***************************************\nMy Coffee and Muffin Shop')
#Write a program that asks user for number of coffee and muffins being purchased
#Then have the user input values then have it display a response prompt
coffeePurchased = int(input("Number of Coffee's bought?\n"))
muffinsPurchased = int(input("Number of Muffins bought?\n"))
espressoPurchased = int(input("Number of Espresso's bought?\n"))
americanoPurchased = int(input("Number of Americano's bought?\n"))
print('***************************************\n\n***************************************')
print('My Coffee Shop Receipt')
Coffee = int(5)
Muffin = int(4)
#two new items on menu
Espresso = int(3)
Americano = int(4)
# multiply the new items by user input
cof = Coffee * coffeePurchased
muf = Muffin * muffinsPurchased
esp = Espresso * espressoPurchased
ame = Americano * americanoPurchased
import decimal
from decimal import Decimal
x = Decimal('0.00')
tax = (float(cof + muf + esp + ame) * .06)
total = (float(cof + muf + esp + ame + tax))
print(coffeePurchased,"Coffee at $",Coffee,'each: $',cof)
print(muffinsPurchased,"Muffins at $",Muffin,'each: $',muf)
print(espressoPurchased,"Espresso at $",Espresso,'each: $',esp)
print(americanoPurchased,"Americano at$",Americano,'each: $',ame)
print('6% tax: $',tax)
print('---------')
print('Total: $',total)
print('Thank you! :D')
print('***************************************')
