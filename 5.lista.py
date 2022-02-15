# Lists
# declaration and length
# -mutable with append, remove
# -sorting
# - sum, min, max

empty = []
print(empty)

friends = ["mickey", "ben", "Tim", "jazzy", "junior"]
print(friends)
print(friends[1:-1]) #does not include first and last
print(friends[1::2]) #every other item
print(friends[::2]) #every other item from index 0


friends.append('mummy')
print("mummy added", friends)

friends.remove('mickey')
print("mickey removed", friends)


friends.sort()
print("sorted", friends)

friends.sort(key=str.lower) #sort by lowercase else uppercase will alwauys come before lowercase
print(friends)



colors = ["red", "orange", "blue", "pink"]
print(colors)

alpabetical = sorted(colors) #sorted is an inbuild function
print(colors)
print(alpabetical)

alpabetical = sorted(colors, reverse=True)
print(alpabetical)

reversedColors = reversed(colors)  #inbuilt
print(list(reversedColors)) #pass it thorugh list to see it



scores = [158, 210, 166, 76]
print(scores)

teamScore = sum(scores) #in uilt
print(teamScore)

highestScore = max(scores)
print(highestScore)

lowestScore = min(scores)
print(lowestScore)

averageScores = sum(scores) / len(scores)
print(averageScores)