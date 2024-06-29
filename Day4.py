# print("hello")
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# print(num2/num1)



# type casting
# int(), float(),str(),dict(),list(),tuple(),set()

# var = 10.2
# # var = float(var)
# var = int(var)
# print(var)
# print(type(var))


# num1 = input("enter first number: ")
# num2 = input("enter second number: ")

# num1 = int(num1)
# num2 = int(num2)
# print(num1)
# print(num2)
# print(type(num1))
# print(type(num2))

# ###  / division are return decimal value
# ###  // floor division are no return decimal value

#####  **
#####  **  exponential are power of the value

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# # print(num1//num2)
# # print(num1**num2)
# print(num1%num2)

# num = 10
# # # num+=5
# # # num +=3
# # num *=3
# # # num-=3

# print(num)

# x = 15
# x%=3
# print(x)

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# print(num1==num2)
# print(num1!=num2)
# print(num1>num2) # 5>10 = True
# print(num1<=num2) # 5<10 = True

# 10<9 = False
# 10<10 = False
# 10<=10 = True
# 10=>10 True


#####>>>>> conditional statement >>>>>>>>>>>>>>>>>>>>>

# relative = input("are you realtive of my family in house:")

# if relative == "y":
#     print("welcome")
# elif relative == "padosi":
#     print("no need to welcome")    
# else:
#     print("your are not welcome")


# program

# guest_list = ["kumkum","rohit","mohit","khushbu","jhunki"]
# name = input("Please enter your name: ")

# if name in guest_list:
#     print("welcome")
# else:
#     print("not welcome")    
    
 
guest_list = ["kumkum","rohit","mohit","khushbu","jhunki"]
name = input("Please enter your name: ")    
if name not in guest_list:
    print("not welcome")
else:
    print("welcome")       