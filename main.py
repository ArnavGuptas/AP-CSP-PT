#Weighted Average Calculator
numberofInput = input("Please enter number of grades to be proccesed: ")
numList = []
for i in range(1, int(numberofInput)+1):
    numInput = input("Enter grade number " + str(i) + ": ")
    numList.append(numInput)

def findMean(numList):
    meanOutput = []
    mean = 0
    for each in numList:
        mean += int(each)
        mean = mean / len(numList)
    meanOutput = "Mean: " + str(round(mean, 4))
    return meanOutput

def findMedian(numList):
    medianOutput=[]
    numList.sort()
    medianIndex = len(numList)-1
    medianIndex = medianIndex / 2
    if len(numList) % 2 != 0:
        median = numList[int(medianIndex)]
    else:
        medianNum1 = int(numList[int(medianIndex + 0.5)])
        medianNum2 = int(numList[int(medianIndex - 0.5)])
        median = medianNum1 + medianNum2
        median = median / 2
    medianOutput = "Median: " + str(median)
    return medianOutput

def findMode(numList):
    modeDictionary = {}
    modeDictionaryValues= {}
    modeOutput = {}
    for each in numList:
        modeDictionary[each] = modeDictionary.get(each, 0) + 1
        modeDictionaryValues = list(modeDictionary.values())
    for i in range(0, len(modeDictionary)):
        if modeDictionary[each] == modeDictionaryValues[0]:
            return "No Mode Found"
        else:    
            modeOutput = "Mode: " + max(modeDictionary, key = modeDictionary.get)
    return modeOutput

whichFunction = input("Would you like mean for a balanced average of all grades, median for an idea of the average grade without including outliers as much, or mode for the most average grade?: ")
if whichFunction == "mean":
    print(findMean(numList))
elif whichFunction == "mode":
    print(findMode(numList))
elif whichFunction == "median":
    print(findMedian(numList))
