#The goal of this one is to try to get data over multiple months or at least consolidate the hourly data into daily data
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
dayDict = {}
sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in dataFile:
    line = line.strip()
    lineList = line.split(",") 

    (d1, t1) = lineList[0].split(" ")
    date2 = Date(d1)
    time2 = Time(t1)


    if(date2.getStr() == "2019-01-06"): #For now, we dont want too much data so we're making it stop after the first day
        break
    # 2019-02-28
    # 2020-01-01


    #the key will be a tuple of the date and time, the value will be the energy data
    dataDict[(date2, time2)] = lineList[1:] #slice everything except for the date & time; (key = the date & time, value = the data)
    dateIndex[dIndex].append(date2) #can't use both because the index doesn't exist yet
    timeIndex[dIndex].append(time2)

    ''''''
    for i in range(len(sumList)):
        print
        sumList[i] += int(dataDict[(date2, time2)][i])

    tIndex+=1

    if(tIndex+1==24):
        dayDict[date2.getStr()] = sumList
    


    if(tIndex>=24): #reset the timeIndex every time we get to a new day
        # print("newday. dIndex:" + str(dIndex) + " tIndex:" + str(tIndex))
        # print(dateIndex[dIndex][tIndex-1].getStr())

        ''''''
        sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        dIndex+=1
        dateIndex.append([date2])
        timeIndex.append([time2])
        tIndex=0   



#Start off simple, Try to create a basic energy demand and supply graph
#Line graph with energy demand and supply 


#CREATE x and y lists for lines

# consLineXcoord = 0
        


energyConsFig = figure(width = 1000, title = "Daily Energy Consumption vs. Time", x_axis_label = "Time", y_axis_label = "Energy (MegaWatts)")

energyConsFig.line((0, 0), (0, 10000)) #Yaxis
energyConsFig.line((0, 10000), (0, 0)) #Xaxis


print(dateIndex)
# '''
print("starting Line")
for i in range(len(dateIndex)):
    consDayLineX = []
    consDayLineY = []
    consDayLineFinalCoord = ""

    prodDayLineX = []
    prodDayLineY = []
    prodDayLineFinalCoord = ""


    
    currentXCoord = i * 50
    # for j in range(len(dateIndex[i])): #consumption is the first value in the list
    currentDay = dayDict[(dateIndex[i][0]).getStr()]


    totalDayCons = 0
    for enrgLst in currentDay:
        print(dateIndex[i][0].getStr())
        totalDayCons += enrgLst

    # consumpDayPoint = dayDict[(dateIndex[i][0])] 


    consDayLineX.append(currentXCoord) #X values, for now it's a 1-1 thing
    consDayLineY.append(totalDayCons)
    consLineFinalCoord = int(totalDayCons)

    totalDayProd = 0
    for enrgLst in currentDay:
        totalDayProd += enrgLst

    prodDayLineX.append(currentXCoord) 
    prodDayLineY.append(totalDayProd)     
    prodDayLineFinalCoord = int(totalDayProd)


    energyConsFig.line((currentXCoord, currentXCoord), (0, -100), color = "black", line_width = 2)
    energyConsFig.text(x = currentXCoord-100, y = -500, text = [dateIndex[i][0].getStr()], text_font_size = "7px")
    ''''''

col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
energyConsFig.line(consDayLineX, consDayLineY, line_width = 2, color = col)
energyConsFig.text( x = len(dateIndex) * 5, y = consDayLineFinalCoord, text = ["Energy Consumption"], text_font_size = "7px")

    #for Production
energyConsFig.line(prodDayLineX, prodDayLineY, line_width = 2, color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
energyConsFig.text(x = len(dateIndex) * 5, y= prodDayLineFinalCoord, text = ["Energy Production"], text_font_size = "7px")

# show(energyConsFig)
# '''
        