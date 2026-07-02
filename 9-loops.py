# # print number from 1 to 100
# for i in range(1,101):
#     print(i)

# # print number from 100 to 1
# for j in range(100,0,-1):
#     print(j)
    
# # print all even number from 1 to 100
# for i in range(0,101,2):
#   print(i)

# # print all odd number from 1 to 100
# for i in range(1,100,2):
#    print(i)

# print the sum of first n natural number
# n=10
# total_sum=0
# for i in range(1,n+1):
#     total_sum+=i
#     print(f"the sum of first {n} natural no is:{total_sum}")

# # find the factorial of a no.
# num=int(input("enter a number"))
# factorial=1
# if num==0:
#   print("The factorial you entered")
# else:
#   for i in range (1,num+1):
#     factorial=factorial*i
#     print(f" the factorial of {num} is {factorial}")

# # print the multiplication table of a number
# num=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# # reverse a number
# num=12345
# reversed_num=int(str(num)[::-1])
# print(reversed_num)

# # print the patterns
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# n=int(input("Enter the number of rows:"))
# for row in range(n):
#     for col in range(n):
#         if col==0 or row==(n-1) or row==col:
#             print("*",end="")
#         else:
#          print(end=" ")
#     print()
