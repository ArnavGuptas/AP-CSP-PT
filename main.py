#Grade Comparison Calculator
numberofInput = input("Please enter number of grades to be proccesed: ")
#Makes sure the input was a number and not a letter or special charecter
while numberofInput.isnumeric() == False:
    numberofInput = input("Please enter number of grades to be proccesed: ")
numList = []
#This loop adds all of the inputs into the list numList
for i in range(1, int(numberofInput)+1):
    numInput = input("Enter grade number " + str(i) + ": ")
    numList.append(numInput)

#This function finds the mean or average of paramter numList
def findMean(numList):
    meanOutput = []
    mean = 0
    for each in numList:
        mean += int(each)
    mean = mean / len(numList)
    meanOutput = "Mean: " + str(round(mean, 4))
    return meanOutput

#This function finds the median of the list, which is the average of the middle two numbers of the list if it were organized from least to greatest
def findMedian(numList):
    medianOutput=[]
    #.sort() organizes the list by least to greatest
    numList.sort()
    #medianIndex is the halfway of the length of the list minus one because indexs start at 0
    medianIndex = len(numList)-1
    medianIndex = medianIndex / 2
    #This if statement checks if the list has an odd or even length because if it is odd, the middle number is the median, but if it is even the mean of the middle two numbers is the median
    #%2 is modulo 2 because if the remainder after dividing by 2 is 0 then the number is even, if not its odd 
    if len(numList) % 2 != 0:
        median = numList[int(medianIndex)]
    else:
    #Since if the length is even medianIndex will end in .5, adding and subtracting 0.5 gives the index of the two middle numbers
        medianNum1 = int(numList[int(medianIndex + 0.5)])
        medianNum2 = int(numList[int(medianIndex - 0.5)])
        median = medianNum1 + medianNum2
        median = median / 2
    medianOutput = "Median: " + str(median)
    return medianOutput

#This function finds the mode, which is the most common number in the list
def findMode(numList):
    modeDictionary = {}
    modeDictionaryValues= {}
    modeOutput = {}
    for each in numList:
        #.get() gets the value of the key provided in the first parameter, and the second parameter provides a default value if the key doesn't exist. The +1 is there because if the key is there already, then the value is increased by 1
        #The keys are the numbers that are in numList, and the values are the number of times they show up
        #So in short what the below line does is check for a key, and if it is there it adds one to it's value, and if it isn't it will create it with value 0
        modeDictionary[each] = modeDictionary.get(each, 0) + 1
        modeDictionaryValues = list(modeDictionary.values())
    #If there is not a greater number of one number then others then the function returns no mode 
    for i in range(0, len(modeDictionary)):
        #.count() returns how many instances of a value there is in a list, and if there is more then one number with the same count then there is no mode
        if modeDictionaryValues.count(modeDictionary[each]) > 1:

            return "No Mode Found"
        else:    
        #max() returns the highest value in the dictionary, and the value of the count of each number, so the number with the highest count is the mode
            modeOutput = "Mode: " + max(modeDictionary)
    return modeOutput
#Gives you the mean, median, or mode of the number dependging on input
whichFunction = input("Would you like mean for a balanced average of all grades, median for an idea of the average grade without including outliers as much, mode for the most average grade?, or all of them: ")
if whichFunction == "mean":
    print(findMean(numList))
elif whichFunction == "mode":
    print(findMode(numList))
elif whichFunction == "median":
    print(findMedian(numList))
else:
    print(findMean(numList), ", ", findMedian(numList), ", ",findMode(numList))
