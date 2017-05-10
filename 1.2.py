def bank (n, m, years):
    percent = 1.1
    amount = n
    for i in range(years):
        amount = amount * percent + m
    return amount

print( bank(1000000, 100000, 2) )
