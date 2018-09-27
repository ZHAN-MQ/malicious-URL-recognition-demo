import numpy as np

def sigmoid(inX):
    return 1 / (1 + np.exp(-inX))

#stochastic gradient ascent
def stocGradAscent(dataMatrix,classLabels,numIter):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex=list(range(m))
        for i in range(m):
            alpha = 4 / (1 + i + j) + 0.01 #alpha must be greater than a constant term, to ensure that new data still has some influence
            randIndex = int(np.random.uniform(0, len(dataIndex))) #Reduce cyclical fluctuations
            h=sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * dataMatrix[randIndex] * error
            del(dataIndex[randIndex])
    return weights 
 
def classifyVector(inX, trainWeights):
    prob = sigmoid(sum(inX * trainWeights))
    if prob > 0.5:
        return 1
    else:
        return 0

def Test():
    frTrain = open('url-train.txt')
    frTest = open('url-test.txt')
    trainSet = []
    trainLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split(',')
        lineArr = []
        for i in range(7):
            lineArr.append(float(currLine[i]))
        trainSet.append(lineArr)
        trainLabels.append(float(currLine[7]))
    trainWeights = stocGradAscent(np.array(trainSet),trainLabels, 9)
    Count = 0
    numTestVec=0
    for line in frTest.readlines():
        numTestVec += 1
        currLine = line.strip().split(',')
        lineArr = []
        for i in range(7):
            lineArr.append(float(currLine[i]))
        if classifyVector(np.array(lineArr),trainWeights) == int(currLine[7]):
            Count += 1
    correctRate=(float(Count) / numTestVec)
    print('the correct rate of this test is : %f' %correctRate)
    return correctRate

def multiTest():
    numTests = 5
    correctSum = 0
    for i in range(numTests):
        correctSum += Test()
    print('after %d iterations the average correct rate is: %f'%(numTests, correctSum/float(numTests)))

multiTest()