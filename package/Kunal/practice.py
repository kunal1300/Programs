# # fib=[0,1]
# fib=[0,1]
# for i in range(10):
#     fib.append(fib[i]+fib[i+1])
# print(fib)
# # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# # prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]





# for i in range(10, 20):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')
# # Output: 11 13 17 19



# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]

# for i in list1:
#     square=i**2
#     list2.append(square)
# print(list2)

# import random
# my_list=[]  # Initialize an empty list
# for i in range(10): # Loop 10 times
#     random_int = random.randint(1, 100)  # generates a random integer between 1 and 100
#     my_list.append(random_int)
# for j  in my_list:
#     if j%2==0:
#         print(j, end=' ')


# import random
# random_list=[random.randint(1,100)for i in range(10)]
# print('random list:',random_list) 
# print('unique list in ascending order:',sorted(random_list,reverse=False))
# print('sorted list in descending order:',sorted(random_list,reverse=True))
# unique_list=list(set(random_list))
# print('unique list:',unique_list)

# students = [
#     {'name': 'Alice', 'score': 88},
#     {'name': 'Bob', 'score': 72},
#     {'name': 'Charlie', 'score': 95},
#     {'name': 'David', 'score': 65},
#     {'name': 'Eve', 'score': 78}
# ]
# sorted_students =sorted (students,key =lambda x:x['score'],reverse=True)
# print('students in descending order:',sorted_students)
# for student in sorted_students:
#     print(student)

# def transpose_matrix(matrix):
#     transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     return transposed

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed = transpose_matrix(matrix)
# print("Original matrix:")
# for row in matrix:
#     print(row)
# print("Transposed matrix:")
# for row in transposed:
#     print(row)

# tup=tuple(i for i in range(1,10))
# print(tup)
    
# print(tup[0])
# print(tup[len(tup)//2])
# print(tup[-1])

# matrix = (
#     (1,2,3),
#     (4,5,6),
#     (7,8,9))
# print("Matrix")
# for i in matrix:
#     print(i)


# add=lambda a,b:a+b  
# print(add(10,20))

number =[1,2,3,4,5]

# def square(number):
#     return number**2

# print(square(3))
#/map
#print(list(map(lambda x:x**2,number)))

print(list(map(lambda x:x*2,number)))

words=["apple","bannana","peears","orange"]

print(list(map(str.upper,words)))

# def fun(num):
#     if num%2==0:
#         return True

# print(fun(20))


# def fun(*args,**kwargs):
#     for i in args:
#         print(i)

#     for key,value in  kwargs.items():
#         print(key,value)

# fun(1,2,4,name ="kunal",age=23)