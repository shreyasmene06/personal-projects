import random
year=random.randint(1993,2018)
if(year%4==0 and year%100!=0 or year%400==0):
    print("given year is a leap year")
else:
    print("given year is not a leap year")
    