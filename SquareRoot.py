# Get approximate square root of floating point number
# 1 ask for the floating point number
number = input("Please type a positive floating point number: ")
def newtonsqrt(number)
def approx = 0.5*number
better=0.5*(approx+number/approx)
while better!=approx:
    approx=better
    better=0.5*(approx+number/approx)
    return approx
print(newtonsqrt(64))   