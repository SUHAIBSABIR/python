# print("hello world")
# print("my name is suhaib","my age is 12")
# print("my age is 12")
# name="suhaib"
# age=23
# print(age,name)

# num1=2
# num2=10
# print(num1+num2)

# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# a=int("2")
# b=2
# int(a)
# print(a+b)


# aa=int(input("entre num"))
# a1=int(input("entre num"))
# a2=int(input("entre num"))
# a3=int(input("entre num"))

# area=aa*a1*a2*a3
# print(area)


var1 =float(input())
var2 =float(input())
avg=(var1+var2)/2
print(avg)

# Write a Python program to check if a number is positive, negative, or zero.
# Write a Python program to find the maximum of three numbers.
# Write a Python program to check if a year is a leap year or not.
# Write a Python program to check if a character is a vowel or a consonant.
# Write a Python program to check if a given string is a palindrome or not.


user=int(input("entre number to check"))

if user<0:
    print("num less")
elif user>0:
    print("greather")
elif user==0:
    print("equal")


    print("helloworld")

    user1=int(input("entre number"))
user2=int(input("entre number"))
user3=int(input("entre number"))


if user1>=user2 and user1> user3:
    print("user1 in greather")

elif user2>user1 and user2>user3:

    print("num2 is greather")


    weather=str(input("entre the weather"))

if weather == "cold":
    print("Wear warm clothes and drink coffee")
elif weather == "hot":
    print("Drink water")
else:
    print("Lovely day")


    num='suhaib'
    for i in num:
        print(i)

    num = "suhaib"
for i in num:
    print(i)
num = "kjj"
for n in num:
    print(n)


    num2= 2
    if num2%2==0:
        print("even")
    else:
        print("odd")
    
        for lo in range(1,3):
        print(lo)


        username="suhaib"
        password=1234
       
for i in range(1,3):
    input1=input("name")
    input2=int(input("password"))
    if input1==username and password==input2:
        print("login ")
        break
    elif (username!=input1):
        print("i user")
    elif(password!=input2):
        print("i pass")
        if range==2:
            print ("you cant login")










password = 1234

for i in range(1, 4):
    userinput = input("Enter username: ")
    userpassword = int(input("Enter password: "))

    if username == userinput and password == userpassword:
        print("Login successful")
        break
    elif username != userinput:
        print("Incorrect username")
    elif password != userpassword:
        print("Incorrect password")

if i == 3:
    print("You can't login now")



