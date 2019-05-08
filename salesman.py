array = [0]

def readFile(name):
    file = open(name)
    file = file.read()
    var = file.splitlines()

    for line in range(len(var)):
        if line%2 != 0:
            word = var[line].split(' ')

    for i in range(len(word)):
        word[i] = int(word[i])
        array.append(word[i])
    return array


name = 'houses.txt'
readFile(name)


n = len(array)

k = int(input("Enter value of k: "))


val = []
back = []

#take care of the case where k == n
#delivers the same result as of previous value
if k == n-1:
    k-=1

#add the first k+1 elements
for i in range(k + 2):
    val.append(array[i])
    back.append(0)


maxValue = val[1] #assume the first value is max
maxIndex = 1 #the first index



for i in range(k + 2, n):
    val.append(array[i] + maxValue) #add the array value with the current maxValue
    i = i - k #go back
    back.append(maxIndex) #add the index
    if val[i] > maxValue: #update the maxValue
        maxValue = val[i]
        maxIndex = i


#add a for loop to find the max
for i in range(n):
    if val[i] > maxValue:
        maxValue = val[i]
        maxIndex = i


#for back tracking of indexes
track = []
while maxIndex != 0:
    track.append(maxIndex)
    z = maxIndex - back[maxIndex]
    maxIndex = maxIndex - z

#print the number of houses
for i in range(len(track)-1,-1,-1):
    print("House: "+str(track[i]))

#print the total
print("Total Sale: "+str(maxValue))


