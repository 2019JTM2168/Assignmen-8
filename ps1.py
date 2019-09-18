# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of bits : "))

# iterating till the range
for i in range(1, n):
    ele = int(input())

    lst.append(ele)  # adding the element
print(lst)

for i in lst:
    print(lst[i])

# def convert(string):
#     li=list(string.split(" "))
#     return li
#
# x=input("Enter binary data :")
# count=0
#
# y=print(convert(x))

# x=x.split('')
#
# for items in x
#     print (i)
#     if items==1
#         count++
#     if count%2==0
#         p=1
#     if count%2==1
#         p=0
# print(p)