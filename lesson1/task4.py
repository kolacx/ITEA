def bank(summ, year, percent):

    for i in range(year):
        summ += summ * ( percent / 100 )
        
    return summ

print(bank(1000, 3, 1.2))