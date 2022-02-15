# processing lists
#-any, all
#-filter
#-map
#zip
#-custom sort

from re import A


print("all() - any item that is false")
title1 = ["Mr", "Mrs", "Ms"]
title2 = ["Mr", "Mrs", "Ms", ""]
title3 = []
print(all(title1))
print(all(title2))
print(all(title3))


print("any - any itme to be true")
feedback1= ['','', '', ''] 
feedback2= ['So much info','', '', '']
feedback3 = []
print(any(feedback1))  # False not any content in list
print(any(feedback2)) #True - 
print(any(feedback3))


scores = [89, 90, 67, 89, 97, 87, 60]

# find out whisch scores got an A
def isA(num):
    return num >= 90
aScores = filter(isA, scores)
print(aScores) #shoes as a filter object reference
print(list(aScores))


def getGrade(num):
    if(num >= 90):
        return "A"
    elif(num < 90 and num >= 80):
        return 'B'
    elif(num < 80 and num >= 70):
        return 'C'
    elif(num < 70 and num >= 60):
        return 'D'
    else: 
        return 'F'

grades = map(getGrade, scores)
letterGrade = list(grades)
gradeZipped = zip(letterGrade, scores)
print(list(gradeZipped))
# [('B', 89), ('A', 90), ('D', 67), ('B', 89), ('A', 97), ('B', 87), ('D', 60)]


users = [
    {"id": 1, 'displayName': 'Mickey T', "email":"mickey@gmail.com"},
    {"id": 2, 'displayName': 'Ben T', "email":"ben@gmail.com"},
    {"id": 3, 'displayName': 'tim A', "email":"tim@gmail.com"}
]
print(users)

def sorter(user):
    return user['displayName'].lower() #naturally sorts by uppercase so tag loer if you wnat it to sort by lower


users.sort(key=sorter)
print(users)

reversedUsers = sorted(users, key=sorter, reverse=True)
print(reversedUsers)