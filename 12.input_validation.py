#Input Va;odatopm
#-prompt
#-handle empty string
#-make it a number
#-handle exceptions
#-require valid input
# age = 1
# while age:
#     age = input("What's your age? ")

#     if age:
#         try:
#             age = int(float(age))
#             if age > 0 and age < 120:
#                 print(f"Cool! You are {age} years old")
#             else:
#                 print('Out of range. Please try again')
#         except:
#             print("Please enter a number")

nums = set([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(sum(nums))
nums = ['1', '2', '3', '4', '5', '4', '3', '2', '1']
print(sum(nums))
