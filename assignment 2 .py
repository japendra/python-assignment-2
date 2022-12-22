#ans 1
fact=('Python is a case sensitive language')
print(len(fact))
print(fact[::-1])
print(fact[10:26])
Fact=("Python is a case sensitive language")
Fact=Fact.replace("a case sensitive","object oriented")
print(Fact)
s=fact.find("a")
print(s)
x=fact.replace(" ",'')
print(x)

#ans4
a=int(input('Enter the First Number:-'))
b=int(input('Enter the Second Number:-'))
c=int(input('Enter the Third Number:-'))
if a>b and a>c :
    print(a)
elif b>c and b>c :
    print(b)
else:
    print(c)

#ans5
string = input("Enter a string: ")
if "name" in string:
    print("The word 'name' is present in the string.")
else:
    print("The word 'name' is not present in the string.")

#ans6
a=int(input('Length of first side of the triangle:-'))
b=int(input('Length of second side of the triangle:-'))
c=int(input('Length of third side of the triangle:-'))
if (a+b > c) and (b+c > a) and (c+a > b):
    print("Yes")
else:
    print("No")