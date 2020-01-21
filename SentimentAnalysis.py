#BurgundyWalrus
#09/28/2019
#Challenge number 2
import numpy as np
import matplotlib.pyplot as mplot
import math


sentifile = open("sentiment_lex.csv", "r")
sentidata = sentifile.read()
sentidata = sentidata.split("\n")
sentidata.pop()
sentidata.pop()
sentidict = {}
datadict = {}
data1= []
neg = 0
wneg = 0
neu = 0
wpos = 0
pos = 0

for x in range(0, len(sentidata)):
    sentidata[x] = sentidata[x].split(",")
    sentidict[sentidata[x][0]] = np.float64(sentidata[x][1])
    

userinput = input("Enter the name of the series(a or bg) : ")
userinput = userinput.lower()
if (userinput == 'a') :
    for x in range (100, 122):
        file = open("a{}script.txt".format(x+1), "r")
        data = file.read()
        
        data = data.replace("," , " ")
        data = data.replace(".", " ")
        data = data.replace("[" , " ")
        data = data.replace("]" , " ")
        data = data.replace("-" , " ")
        data = data.replace(":" , " ")
        data = data.replace("?" , " ")
        data = data.replace("!" , " ")
        data = data.replace("." , " ")
        data = data.replace("\n", " ")
        data = data.replace(")" , " ")
        data = data.replace("(" , " ")
        data = data.replace("<" , " ")
        data = data.replace(">" , " ")
        data = data.replace("'" , "")
        data = data.replace("\"" , "")
        data = data.split(" ")
        
        for x in range (0, len(data)) : 
            if (data[x] != ""):
                data1.append(data[x].lower())
                
    for x in range (0 , len(data1)):
        datadict[data1[x]] = data1.count(data1[x])
    
    for keys in sentidict.keys():
        for keys2 in datadict.keys():
            if keys2 == keys :
                if (sentidict[keys] >= -1.0) and (sentidict[keys] < -0.6):
                    neg = neg + datadict[keys2]
                elif (sentidict[keys] >= -0.6) and (sentidict[keys] < -0.2):
                    wneg = wneg + datadict[keys2]
                elif (sentidict[keys] >= -0.2) and (sentidict[keys] <= 0.2):
                    neu = neu + datadict[keys2]
                elif (sentidict[keys] > 0.2) and (sentidict[keys] <= 0.6):
                    wpos = wpos + datadict[keys2]
                elif (sentidict[keys] > 0.6) and (sentidict[keys] <= 1.0):
                    pos = pos + datadict[keys2]
                    
    xaxis = ['Neg', 'W.Neg', 'Neu','W.Pos','Pos']
    yaxis = [math.log10(neg) , math.log10(wneg), math.log10(neu), math.log10(wpos), math.log10(pos)]
    
    mplot.xlabel("Sentiment")
    mplot.ylabel("log word count")
    mplot.title("Sentiment Analysis for Series \"a\"")
    mplot.bar(xaxis, yaxis)

    
if (userinput == "bg"):
    for x in range (100, 113):
        file = open("bg{}script.txt".format(x+1), "r")
        data = file.read()
        
        data = data.replace("," , " ")
        data = data.replace(".", " ")
        data = data.replace("[" , " ")
        data = data.replace("]" , " ")
        data = data.replace("-" , " ")
        data = data.replace(":" , " ")
        data = data.replace("?" , " ")
        data = data.replace("!" , " ")
        data = data.replace("." , " ")
        data = data.replace("\n", " ")
        data = data.replace(")" , " ")
        data = data.replace("(" , " ")
        data = data.replace("<" , " ")
        data = data.replace(">" , " ")
        data = data.replace("'" , "")
        data = data.replace("\"" , "")
        #data = data.replace("" , "")
        data = data.split(" ")
        
        for x in range (0, len(data)) : 
            if (data[x] != ""):
                data1.append(data[x].lower())
        
    for x in range (0 , len(data1)):
        datadict[data1[x]] = data1.count(data1[x])
    
    for keys in sentidict.keys():
        for keys2 in datadict.keys():
            if keys2 == keys :
                if (sentidict[keys] >= -1.0) and (sentidict[keys] < -0.6):
                    neg = neg + datadict[keys2]
                elif (sentidict[keys] >= -0.6) and (sentidict[keys] < -0.2):
                    wneg = wneg + datadict[keys2]
                elif (sentidict[keys] >= -0.2) and (sentidict[keys] <= 0.2):
                    neu = neu + datadict[keys2]
                elif (sentidict[keys] > 0.2) and (sentidict[keys] <= 0.6):
                    wpos = wpos + datadict[keys2]
                elif (sentidict[keys] > 0.6) and (sentidict[keys] <= 1.0):
                    pos = pos + datadict[keys2]
                    
    xaxis = ['Neg', 'W.Neg', 'Neu','W.Pos','Pos']
    yaxis = [math.log10(neg) , math.log10(wneg), math.log10(neu), math.log10(wpos), math.log10(pos)]
    
    mplot.xlabel("Sentiment")
    mplot.ylabel("log word count")
    mplot.title("Sentiment Analysis for Series \"bg\"")
    mplot.bar(xaxis, yaxis)
    