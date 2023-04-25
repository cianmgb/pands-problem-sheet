#Ask for the bank account number
Accountstring = input("Please enter your account number ")
#Get the last 4 digits
AccountShowingonlylast4digits = Accountstring[-4:].rjust(len(Accountstring), 'X')
#Print the last four digits only, with X replacing all recurring digits
print(AccountShowingonlylast4digits)