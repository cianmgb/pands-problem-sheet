#Ask for two cent amounts
Value1 = int(input("Enter amount1(in cent): "))
Value2 = int(input("Enter amount2(in cent): "))
#Add the two amounts in cent
TotalValue = Value1 + Value2
#Convert total cents to euro and cent
euro = TotalValue // 100
Cent = TotalValue % 100
#Print in Human Readable format
print("The sum of these is €{:d}.{:02d}".format(euro, Cent))