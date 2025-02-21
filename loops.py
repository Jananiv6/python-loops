# 1. to find the greatest of the number
m1=float(input("Enter the number"))
m2=float(input("Enter the number"))
m3=float(input("Enter the number"))
# m1=93
# m2=24
# m3=43
if m1>m2 and m1>m3:
    print("m1 is greater")
elif m2>m1 and m2>m3:
    print("m2 is greater")
elif m3>m1 and m3>m2:
    print("m3 is greater")
else:
    print("All are Equal")

# 2.To find the leap year

year=int(input("Enter the Year"))
if (year%4==0   and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"not a leap year")


# 3.to find vowel, consonant r neither
user=str(input("Enter the input"))
vowel="a,e,i,o,u,A,E,I,O<,U"
constant="isalpha()"
if user in vowel:
    print("vowel",vowel)
elif user.isalpha():
    print("constant",constant)
else:
    print("Neither")


#4. To find the grade
marks=float(input("Enter the marks"))
if marks>90 and marks<100:
    print("Grade A")
elif marks>80 and marks<89:
    print("Grade B")
elif marks>70 and marks<79:
    print("Grade C")
else:
    print("Fail")


# 5.To  form a triangle

a=float(input("Enter the value"))
b=float(input("Enter the value"))
c=float(input("Enter the value"))
if ((a+b>c) and (b+c>a) and (c+a>b)):
    print("form a valid triangle")
else:
    print("can't form a valid triangle")

