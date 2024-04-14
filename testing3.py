#The goal of this one is to try to get data over A SINGLE month
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import random

#Removed from Line1: DateTime,Consumption,Production,Nuclear,Wind,Hydroelectric,Oil and Gas,Coal,Solar,Biomass



class Date:
    # self.str, self.dataList
    def __init__(self, s):
        self.strin = s
        self.dataList = list(s.split("-"))#REMINDER: You gotta cast this to a list!!

    def getStr(self):
        return self.strin
        
class Time:
    # self.str, self.dataList
    def __init__(self, s):
        self.strin = s
        self.dataList = list(s.split(":")) #hour, minute, second
    def getHour(self):
        return self.dataList[0]


    def getStr(self):
        return self.strin

        


# print("hello world")
dataDict = {}

#These will be the indexes to loop through keys
dateIndex = [[]]  #is this how you make a list inside of a list
timeIndex = [[]]


#plan: create an object called time to store the time, then create a dictionary with the time as keys and the energies as values stored in a list. Then maybe give the time a function that lets it iterate sequentially
dIndex = 0
tIndex=0

dataFile = open("electricityConsumptionAndProductioction 2.csv", "r")
''''''
dayDict = {} #dictionary, the KEY is the date string. the Value should be a list of integers

for line in dataFile:
    line = line.strip()
    lineList = line.split(",") 

    (d1, t1) = lineList[0].split(" ")
    date2 = Date(d1)
    time2 = Time(t1)


    if(date2.getStr() == "2019-02-01"): #For now, we dont want too much data so we're making it stop after the first day
        break
    # 2019-01-06
    # 2019-02-28
    # 2020-01-01


    #the key will be a tuple of the date and time, the value will be the energy data
    dataDict[(date2, time2)] = lineList[1:] #slice everything except for the date & time; (key = the date & time, value = the data)
    dateIndex[dIndex].append(date2) #can't use both because the index doesn't exist yet
    timeIndex[dIndex].append(time2)



    sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(sumList)):
        # print
        sumList[i] += int(dataDict[(date2, time2)][i])
        # print(dataDict[(date2, time2)][i]) #this works
    if d1 not in dayDict:
        dayDict[d1] = sumList # if it's not already there, add the date to the sumList
    else:
        for i in range(len(sumList)): #add everything to that day's list
            dayDict[d1][i] += sumList[i]


    tIndex+=1

    # if(tIndex+1==24):
    #     dayDict[date2.getStr()] = sumList
    


    if(tIndex>=24): #reset the timeIndex every time we get to a new day
        # print("newday. dIndex:" + str(dIndex) + " tIndex:" + str(tIndex))
        # print(dateIndex[dIndex][tIndex-1].getStr())

        ''''''
        # sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        dIndex+=1
        dateIndex.append([date2])
        timeIndex.append([time2])
        tIndex=0   
'''
#DEBUGGING
print("list the days")
for i in range(len(dateIndex)):
    print(dateIndex[i][0].getStr())
    print(dayDict[dateIndex[i][0].getStr()]) #proves that this works
'''


#Start off simple, Try to create a basic energy demand and supply graph
#Line graph with energy demand and supply 


#CREATE x and y lists for lines

# consLineXcoord = 0
        

divisionReduce = 10**2
length = 1000
height = 2500
iScale = length/len(dateIndex)
# iScale = 1

energyConsFig = figure(width = 2000, title = "Daily Energy Consumption vs. Time in Romania (2019)", x_axis_label = "Time", y_axis_label = "Energy (Megawatts) * " + str(divisionReduce))

energyConsFig.line((0, 0), (0, 2500), line_width = 2) #Yaxis
energyConsFig.line((0, length), (0, 0), line_width = 2) #Xaxis


# '''
print("starting Line")
consDayLineX = []
consDayLineY = []
consDayLineFinalCoord = ""

prodDayLineX = []
prodDayLineY = []
prodDayLineFinalCoord = ""
for i in range(len(dateIndex)):



    currentXCoord = i*iScale #subject to change to scale the graph

    currentDayString = dateIndex[i][0].getStr() #loop through all of the days

    consDaily = dayDict[dateIndex[i][0].getStr()][0]/divisionReduce  #the 0 index is consumption
    consDayLineX.append(currentXCoord) 
    consDayLineY.append(consDaily)
    consLineFinalCoord = int(consDaily) #here for the labelling of graphs

    prodDaily = dayDict[dateIndex[i][0].getStr()][1]/divisionReduce  #the 1 index is production, divide by divisionReduce cuz teh numbers were too big
    # print(prodDaily)
    prodDayLineX.append(currentXCoord) 
    prodDayLineY.append(prodDaily)     
    prodDayLineFinalCoord = float(prodDaily)


    energyConsFig.line((currentXCoord, currentXCoord), (0, -100), color = "black", line_width = 1) #the tick markers
    energyConsFig.text(x = currentXCoord, y = -100, text = [dateIndex[i][0].getStr()], text_font_size = "7px", angle = -3.14/2)
    ''''''

    #Adding Month Markers
    if(i>0 and not (dateIndex[i][0].dataList[1] == dateIndex[i-1][0].dataList[1])): #0, 1, 2
        energyConsFig.line((currentXCoord, currentXCoord), (0, height), color = "black", line_width = 2)


# colorRand = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
energyConsFig.line(consDayLineX, consDayLineY, line_width = 2, color = "red")
# energyConsFig.text(x = len(dateIndex) * iScale, y= consDayLineFinalCoord, text = ['Energy Production'], text_font_size = "70px", text_color = "blue")
# energyConsFig.text(x = 0-16, y= dayDict[dateIndex[0][0].getStr()][0]/divisionReduce, text = ['Energy Consumption'], text_font_size = "7px", text_color = "red")
energyConsFig.text(x = 0, y= 2400, text = ['Energy Consumption'], text_font_size = "15px", text_color = "red")


    #for Production
energyConsFig.line(prodDayLineX, prodDayLineY, line_width = 2, color = "blue")
# energyConsFig.text(x = len(dateIndex) * iScale, y= prodDayLineFinalCoord, text = ['Energy Production'], text_font_size = "7px", text_color = "blue")
energyConsFig.text(x = 0, y= 2400-100, text = ['Energy Production'], text_font_size = "15px", text_color = "blue")


show(energyConsFig)
# '''
        