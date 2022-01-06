
#Task 1
#Taken from https://www.geeksforgeeks.org/python-program-for-compound-interest/
#Formula to calculate compound interest annually is given by:
#A = P(1 + R/100) t
#Compound Interest = A – P
#Where:
#A is amount
#P is principle amount
#R is the rate and
#T is the time span

def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
compound_interest(2000, 5.25, 10)

#Task 2
def calcPercent(num,p):
    num=int(input("Number 1: "))
    p=float(input("Percent: "))
    result = num * p;
    print("Percentage is: ", result)

calcPercent(10,10)

#Task 3

def name(s):
    l = s.split()
    new = ""
    for i in range(len(l) - 1):
        s = l[i]
        new += (s[0].upper() + '.')
    new += l[-1].title()
    print(new)

name("Lene Boel Jensen")