list = []
n = int(input("Enter the no of elements: "))
for i in range(0,n):
    num = int(input())
    list.append(num)
print(list)
for num in list:
    if num>=0:
        print(num, end= " ")

