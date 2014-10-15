total = 0 

print "how many numbers do you want to add together?"
userInput = int(raw_input())
for x in range(userInput):
    print "enter a number:"
    numEntered = int(raw_input())
    total= total + numEntered 
print total 

totalList = []

print "how many numbers do you want to add together?"
userInput = int(raw_input())
for x in range(userInput):
    print "enter a number:"
    numEntered = int(raw_input())
    totalList.append(numEntered)
print sum(totalList)

totalList2 = []

print "what number do you want to take the factorial of?"
userInput = int(raw_input())
total = 1
for x in range(1,userInput+1,1): 
    total= total * x 
    
print total 

factors = []
print "pick a number to factor"
userInput = int(raw_input())
for x in range(1,userInput + 1):
    if userInput % x == 0:
        print x 
        
        