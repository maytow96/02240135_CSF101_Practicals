firstlist = [0,2,3,4,5,6,7,8,9]
inverselist = []
array_length = len(firstlist)

index = 0
while index < array_length:
    inverselist.append(firstlist.pop())
    index +=1

print(firstlist)
print(inverselist)

def squarefunction(number:int) ->int:
    result = number **3
    return result
number = 4
for index in range(len(number)):
    
    print(squarefunction(number[index]))