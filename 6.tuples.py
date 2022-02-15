# immutable
# min, max
#cannot append, remove or sort in place


from curses import use_default_colors


a = (1, 2, 3, 4, 5, 6, 7, 8 ,9)
b = ('a', 'b', 'c', 'd', 'e', 'f')
c = 10, 20, 30

print(a)
print(b)
print(c)

shopping = ('applies', 'milk', 'bread')
alphaShopping = sorted(shopping)    #sorted makes it a list
print("now in a list", alphaShopping)
alphaShoopingTuple = tuple(alphaShopping)
print("tuple appied", alphaShoopingTuple)


shopingStops = (
    ["bread", "milk", "eggs"],
    ["picture hooks", "extension cord"]
)

print(shopingStops)
shopingStops[0].append('apples')
print(shopingStops)

users = [
    (1, 'user_a'), 
    (2, 'user_b'),
    (3, "user_b")
    ]

print(users)


scores = (2, 3, 5, 6, 3, 7 )
print(scores)
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
print(sorted(scores))
print(tuple(sorted(scores)))


def minmax(nums):
    return min(nums), max(nums)
myNums = (1, -4, 2, 3.0, 6.9, 0)
print(minmax(myNums))
(lowest, highest) = minmax(myNums) #you can assign the tuple into separate variables
print(lowest)
print(highest)


# tuple of just a single item

empty = ()
print(empty)

single = (1, ) #without adding the comma, it just prints the single digit 1
print(single)