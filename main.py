#Weighted Average Calculator
numberofInput = input("Please enter number of digits to be proccesed: ")
numList = []
for i in range(1, int(numberofInput)+1):
    numInput = input("Enter your " + str(i) + " number: ")
    numList.append(numInput)



def convertToGrades(numList):
    gradesList = []
    for each in numList:
        if each < 60:
            gradesList.append("F")
        elif each < 70:
            gradesList.append("D")
        elif each < 80:
            gradesList.append("C")
        elif each < 90:
            gradesList.append("B")
        else:
            gradesList.append("A")
    return gradesList



def findMeanMedianMode(numList):
    meanMedianModeOutput = []
    mean = 0
    for each in numList:
        mean += int(each)
        mean = mean / len(numList)
    meanMedianModeOutput.append("Mean: " + str(round(mean, 4)))
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
    meanMedianModeOutput.append("Median: " + str(median))

    meanDictionary ={}
    for each in numList:
        meanDictionary[each] = meanDictionary.get(each, 0) + 1
    meanMedianModeOutput.append(meanDictionary)
            


    return meanMedianModeOutput




print(findMeanMedianMode(numList))
