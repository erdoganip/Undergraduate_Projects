#Ipek Erdogan, 150130102
import re
import matplotlib.pyplot as plt
import numpy as np

pairs = []
firstcl = []
secondcl = []
totalx1 = 0
totaly1 = 0
totalx2 = 0
totaly2 = 0
squaredtotalx1 = 0
squaredtotaly1 = 0
squaredtotalxy1 = 0
squaredtotalx2 = 0
squaredtotaly2 = 0
squaredtotalxy2 = 0


with open('classification_train.txt','r') as classfile:    
    data = np.loadtxt('classification_train.txt',delimiter='\t',skiprows=1)
    plt.scatter(data[:,0],data[:,1],c=data[:,2])
    plt.show()
    
    firstline = classfile.readline() #To skip the headlines
    for line in classfile:
        if line.strip(): #It seems we have empty lines in our test data. We need to get rid of them
            x = re.split('\t+',line.rstrip()) #split lines according to the tab characters.
            feat1 = x[0]
            feat2 = x[1]
            label = x[2]
            pairs.append([float(feat1),float(feat2),float(label)])
    for element in pairs:
        if(element[2]==0):
            firstcl.append(element) #Our first class is with label 0
        else:
            secondcl.append(element) #Our second class is with label 1
            
#To calculate mean vectors of class 1 and class 2:
for k in firstcl:
    totalx1 += k[0] 
meanx1=totalx1/len(firstcl)

for l in firstcl:
    totaly1 += l[1]
meany1=totaly1/len(firstcl)

print("Mean Vector 1: [",meanx1,meany1,"]")

for m in secondcl:
    totalx2 += m[0]
meanx2=totalx2/len(secondcl)

for n in secondcl:
    totaly2 += n[1]
meany2=totaly2/len(secondcl)

print("Mean Vector 2: [",meanx2,meany2,"]")

#To calculate the convariance martices of class 1 and 2:

print("CONVARIANCE MATRICES \n")

for k in firstcl:
    squaredtotalx1 += (k[0]-meanx1)**2
    squaredtotaly1 += (k[1]-meany1)**2
    
squaredmeanx1=squaredtotalx1/len(firstcl)
squaredmeany1=squaredtotaly1/len(firstcl)

for k in firstcl:
    squaredtotalxy1 += (k[0]-meanx1)*(k[1]-meany1)
    
squaredmeanxy1=squaredtotalxy1/len(firstcl)

matrix1=[[squaredmeanx1,squaredmeanxy1], [squaredmeanxy1,squaredmeany1]]

print("Convariance Matrix of Class 1 is: \n",matrix1[0],"\n",matrix1[1])

for k in secondcl:
    squaredtotalx2 += (k[0]-meanx2)**2
    squaredtotaly2 += (k[1]-meany2)**2
    
squaredmeanx2=squaredtotalx2/len(secondcl)
squaredmeany2=squaredtotaly2/len(secondcl)

for k in secondcl:
    squaredtotalxy2 += (k[0]-meanx2)*(k[1]-meany2)
    
squaredmeanxy2=squaredtotalxy2/len(secondcl)

matrix2=[[squaredmeanx2,squaredmeanxy2], [squaredmeanxy2,squaredmeany2]]

print("Convariance Matrix of Class 2 is: \n",matrix2[0],"\n",matrix2[1])
