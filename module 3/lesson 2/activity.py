def tc(bill,discount):
    total = bill*(1+0.01*discount)
    total = round(total,2)
    print("Please pay BDT",total)

tc(500,10)