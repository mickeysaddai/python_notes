#Sets
#-declare
#- union, intersection, symmetric_difference, difference
#-unique tages
#-users taking two actions

from turtle import pu


a = {1, 2, 3}
b = {3, 4, 5}
print(a)
print(b)

# combine sets 
print(a | b) #{1, 2, 3, 4, 5}
print(a & b) #{3}
print(a - b) #{1, 2} difference so removed the shared items from a set
print(b - a) #{4, 5}
print(a ^ b)  # {1, 2, 4, 5}  #remove the common value form both sets


a = set('bannana')
b = set('scarab')
print(a)  # {'b', 'a', 'n'}
print(b)  # {'a', 's', 'r', 'b', 'c'}
print(a | b)  # {'c', 'a', 'r', 'n', 'b', 's'}

print(a.union(b)) # another way instead of pipe (|) {'r', 'b', 's', 'a', 'c', 'n'}
print(a.intersection(b))  # {'a', 'b'}
print(a.symmetric_difference(b))  # {'c', 's', 'n', 'r'} everyting unique ie not repeated in both
print(a.difference(b))  # whats in a but not in b {'n'}
print(b.difference(a))  # whats in b but not in a {'r', 'c', 's'}

basket = ['apple', 'banana', 'apple', 'orange', 'banana']
print(basket)
print(set(basket))




# using sets for solving real life problem
purchasingEmails = ['mickgmail.com', "tim@gmail.com", "jaz@gmail.com"]
helpEmails = ['bengmail.com', "tim@gmail.com", "junior@gmail.com"]
print(set(purchasingEmails) & set(helpEmails))  # {'tim@gmail.com'}
