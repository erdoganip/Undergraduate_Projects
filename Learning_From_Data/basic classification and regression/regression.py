#Ipek Erdogan, 150130102

import re
import matplotlib.pyplot as plt

pairs = []
xaxis = [] # These two are just for visualization
yaxis = [] # These two are just for visualization
predicts = []

with open('regression_data.txt','r') as regfile:
    firstline = regfile.readline() #To skip the headlines
    for line in regfile:
        if line.strip(): #It seems we have empty lines in our test data. We need to get rid of them
            x = re.split('\t+',line.rstrip()) #split lines according to the tab characters.
            feature = x[0]
            target = x[1]
            pairs.append([float(feature)/1000,float(target)/1000])
            
#Let's plot our data to see what we have more clear.
for i in range(len(pairs)):
    xaxis.append(pairs[i][0])
    yaxis.append(pairs[i][1])
plt.plot(xaxis,yaxis,'go--',markersize=10)
plt.xlabel('Head Size(Features)')
plt.ylabel('Brain Weight(Targets)')
plt.title('Brain Weight According to the Head Size')
plt.show()

#We need to compute our loss according to the comparison of our predicted y values and the y values that dataset gave us at the beginning.
#We will use squared error method to read our loss. 
def lossFunction(m,b,pairs): 
    totalError = 0
    for i in range(0, len(pairs)): 
        totalError += (pairs[i][1] - (m * pairs[i][0] + b)) ** 2 
        return totalError / float(len(pairs))
#We will implement gradient descent method to find global minimum value of our loss function
#Since we have two parameters (m and b), we need to compute partial derivative for each of them
def gradientDescent(pointM,pointB,pairs,learningRate):
    gradientM = 0
    gradientB = 0
    N = float(len(pairs))
    for i in range(0, len(pairs)):
        x = pairs[i][0]
        y = pairs[i][1]
        gradientM += -(2/N) * x * (y - (pointM * x + pointB))
        gradientB += -(2/N) * (y - (pointM * x + pointB))
        m=pointM - (learningRate * gradientM)
        b=pointB - (learningRate * gradientB)
    return [m,b]

def trainingRegModel(pairs,learningRate,itenum):
    finalM=0
    finalB=0
    for i in range(itenum):
        finalM,finalB=gradientDescent(finalM,finalB,pairs,0.001)
    return [finalM,finalB]

def makePrediction(pairs,predicts,valueM,valueB):
    for i in range(len(pairs)):
        yi=pairs[i][0]*valueM + valueB
        predicts.append(yi)

def plotTheModel(valueM,valueB,pairs,predicts):
    xaxis = [] # These two are just for visualization
    yaxis = []
    for i in range(len(pairs)):
        xaxis.append(pairs[i][0])
        yaxis.append(pairs[i][1])
    plt.plot(xaxis,yaxis,'go--',markersize=10)
    plt.xlabel('Head Size(Features)')
    plt.ylabel('Brain Weight(Targets)')
    plt.title('Brain Weight According to the Head Size')
    x = xaxis
    y = predicts
    plt.plot(x,y)
    plt.show()
    
##for 5-fold cross validation, we need to split our dataset into 5 folds and 
##while train our model with 4 folds, test it with the remaining one.
#
def splitDataset(pairs):
    number = int(len(pairs)/5)
    chunks = [pairs[x:x+100] for x in range(0, len(pairs), number)]
    a = chunks[0]
    b = chunks[1]
    c = chunks[2]
    d = chunks[3]
    e = chunks[4]
    return [a,b,c,d,e]

def crossValidation(splits,pairs):
    meanerror=0
    deneme = splits[:]
    number = int(len(pairs)/5)
    i=0
    for element in deneme:
        temppairs = []
        temppredicts=[]
        testing = element[:]
        splits.remove(element) #I'm basically splitting 1 fold from others
        for k in range(len(splits)):
            for j in range(number):
                temppairs.append(splits[k][j])
        print("THIS IS MODEL ",i)
        m,b = trainingRegModel(temppairs,0.001,100000)
        makePrediction(temppairs,temppredicts,m,b)
        plotTheModel(m,b,temppairs,temppredicts)
        print("THE ERROR FOR THIS MODEL IS ")
        a=lossFunction(m,b,testing) # I'm using the loss function to get a test result
        meanerror+=a #To calculate the overall MSE at the end of 5 models
        print(a)
        print("")
        print("")
        splits.insert(i,testing) #I'm giving back the fold i splitted at the beginning
        i+=1
    return meanerror/5
        
splits = splitDataset(pairs)
meanerr5fold = crossValidation(splits,pairs)
print("Our mean square error of 5 models is:",meanerr5fold)



