# in js we create functions that returned other function 

# function greetingMaker(salutation){
#     function greeting(name){
#         return `${salutation} ${name}`
#     }
#     return greeting;

# }

# const hello = greetingMaker("hello");
# console.log(hello("mickey"))



# we can do similar in python
def greeting_maker(salutation):
    def greeting(name):
        return f'{salutation} {name}'
    return greeting
    
hello = greeting_maker("Hello")
hiya = greeting_maker("Hiya")

print(hello("mickey"))
print(hiya("mickey"))

