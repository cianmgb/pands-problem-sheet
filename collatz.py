#Enter the positive integer
number = int(input("Please enter a positive integer: "))
#make sure we finish the sequence if we get to 1
while number != 1:
    print(number, end=' ')
#Write a function to result in Collatz loop (ie if an even number divide by 2, if odd multiply by 3 and add 1)
#add formula to divide by 2 if even number
    if number % 2 == 0:
        number = number // 2
#if not even number we need to multiply by three then add 1
    else:
        number = number * 3 + 1
#this will allow the formula to recur until we get to 1, per line 5 above
print(number)