import math
buy_price = float(input("Enter a buying price >>>"))
sell_price =float(input("Enter a selling price >>>"))

if buy_price <sell_price:
    amount = abs(buy_price-sell_price)
    print("The profit of",amount)

else:
    print("Loss")
