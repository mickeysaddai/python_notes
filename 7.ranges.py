#Ranges
# -declare
# loops


nums = range(10)
print(nums) #range(0, 10)
print(list(nums))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

counters = range(1, 11)
print(list(counters))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#say you want all the 5s to be in your range
fives = range(0, 51, 5)  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(fives))


items = ['a', 'b', 'c']

for i in range(len(items)):
    print(i, items[i])

for i in range(1, 10, 2):
    print(i) #1, 3, 5, 7, 9