
# list1 = [8, 100, 200]
# #        0,   1,   2
#
# print(range(len(list1)))
# print(list(range(4, 10)))

# print(list(range(4, 10, 2)))
# print(list(range(5, 1, -1)))

# 1. null
# 2. [1, 2, 3, 4]
# 3. [5, 4, 3, 2]
# 4. [[5, 1, 1, 1]]

# 3.


# var1 = [x ** 3 for x in range(5)]
# print(var1)

# 1. [1, 8, 27, 64, 125]
# 2. []
# 3. [null, null, null, null]
# 4. [0, 1, 8, 27, 64]
# 5. [[0, 1, 8, 27, 64]]

# 4.


# var2 = [x for x in range(4) if x % 3 == 0]
# print(var2)
# 2 / 3 = 0 rest 2

# 1. 3
# 2. [0, 3, 6]
# 3. [0, 1, 2, 3]
# 4. [0, 3]
# 5. []

# 4.


# var3 = { "a": 1, "b": 2, "c": 3 }
# inv = {v: k for k, v in var3.items()}
# print(inv)

# 1. ['a', 1, 'b', 2, 'c', 3]
# 2. { 1: "a", 2: "b", 3: "c"}
# 3. { "a": "a", "b": "b", "c": "c"}
# 4. Null

# 2.


# var3 = { "a": 1, "b": 2, "c": 3 }
# filtr = {k: v for k, v in var3.items() if v % 2 == 0}
# print(filtr)

# 1. 2
# 2. {}
# 3. {"b": 2}
# 4. {2: "b"}

# 3


# def func1():
#     print(var10)
#
# func1()
# var10 = 10

# 1. 10
# 2. 0
# 3. Eroare, arunca exceptie
# 4. None
# 5 ""

# 3

# class A:
#     def __init__(self, val):
#         self.val = val
#
#     def __str__(self):
#         return self.val
#
# class B(A):
#     def __init__(self, val, name):
#         A.__init__(self, val, name)
#
#     def __str__(self):
#         return self.name
# a = A(10)
# b = B(10, "Shadow")
# print(a)
# print(b)

# 1.  10
#     10
# 2.  10
#     None

# 3. Codul Arunca Exceptie

# 4. <__main__.A object at 0x000001EB43336CE0>
#    <__main__.B object at 0x000001EB43336CE0>
# 5.  10
#     Shadow

# 3.



for i in range(10):
    if i == 3:
        continue
    print(i)


a = set([1, 2, 3, 4, 4, 10, 20, 20, 30, 10, 1])
print(a)

















