#stacks and queues
#interuupiton stack
#processing queue

# Stack
# teller = []
# teller.append('Greet Customer')
# print(teller)
# teller.pop()
# print(teller)
# teller.append('Process Depost')
# print(teller)
# teller.append('Phone Ringing')
# print(teller)
# teller.pop()
# teller.append('Greeting the caller, AnswerQuestion')
# print(teller)
# teller.pop()
# print(teller)


#Quueue
processer = []
processer.append({'type':'page', 'path':'', 'header': [], 'cookies': []})
processer.append({'type':'api', 'function':'', 'parameters':[]})
processer.append({'email':'email', 'add':'mic@gmail.com', 'subject':""})
print("PROCESSOR", processer)

for i in range(len(processer)):
    item = processer.pop(0)
    print('PROCESSING ITEM', item)
    print("REMAINING LIST",processer)



