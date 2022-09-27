# task 1.1
# a = int(input("Input: "))
# print("Output: ")
# for i in range(1, a + 1):
#     print("Number is: ", i, "and cube of the number is: ", i * i * i)
# print()


# task 1.2

# org_list = str(input("Input: "))
# print("Output: ")
# for i in reversed(org_list):
#     print(i)

# task 1.3

# a = int(input("Input: "))
# fact = 1
# for i in range(1, a+1):
#     fact = fact * i
# result = fact
# print("Output: ", result)

# task 1.4
# a = int(input("Input: "))
# summa = 0
# for i in range(1, a+1, 1):
#     summa = summa + i
# print("Output: ", summa)

# task 1.5
# n = int(input("Input : "))
# temp=n
# rev=0
# while(n):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#     if (n<0):
#         n=(-n)
# print("Output: ")
# if(temp==rev):
#     print("True")
# else:
#     print("False")


#task2.1
# rows = int(input("Input rows: "))
# print("Output: ")
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()

#task 2.2
# rows = int(input("Input rows: "))
# print("Output: ")
# for i in range(rows+1):
#     for j in range(i):
#         print(i, end=' ')
#     print()


#task 3.1
# a = int(input("Input1: "))
# b = int(input("Input2: "))
#
# c = b / 100
# sum = a*c
# print("get_discount(", a, ",", b, ") ->", a-sum)

#task 3.2
# n = int(input("Input: "))
# def sum_numbers(n):
#     if n == 1:
#         return 1
#     return n + sum_numbers(n-1)
# print("get_discount(", n, ") ->", sum_numbers(n))

#task 3.3
# a = int(input("Input1: "))
# b = int(input("Input2: "))
# c = int(input("Input3: "))
# print("is_triplet(",a,",",b,",",c,") ->")
# n1=a*a+b*b
# n2=a*a+c*c
# n3=b*b+c*c
# k1=a*a
# k2=b*b
# k3=c*c
# if (n1==k3 or n2==k2 or n3==k1):
#     print("True")
# else:
#     print("False")










