from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import random

#Removed from Line1: DateTime,Consumption,Production,Nuclear,Wind,Hydroelectric,Oil and Gas,Coal,Solar,Biomass



class Date:
    # self.str, self.dataList
    def __init__(self, s):
        self.strin = s
        self.dataList = list(s.split("-"))#REMINDER: You gotta cast this to a list!!

    # def print(self):
    #     return self.dataList
    def getStr(self):
        return self.strin
        
class Time:
    # self.str, self.dataList
    def __init__(self, s):
        self.strin = s
        self.dataList = list(s.split(":")) #hour, minute, second
    def getHour(self):
        return self.dataList[0]
    # def print(self):
    #     return self.dataList

    def getStr(self):
        return self.strin
    # def getListing(self):
    #     tempString = ""
    #     for d in self.dataList:
    #         tempString = tempString + " " + d
        


# print("hello world")
dataDict = {}
#These will be the indexes to loop through keys
dateIndex = [[]]  #is this how you make a list inside of a list
timeIndex = [[]]
    #New plan: create an list with numbers that I can actually just lopp through that is ordered

#plan: create an object called time to store the time, then create a dictionary with the time as keys and the energies as values stored in a list. Then maybe give the time a function that lets it iterate sequentially
dIndex = 0
tIndex=0

dataFile = open("electricityConsumptionAndProductioction 2.csv", "r")
# previousDate = "2019-01-01"                 #∆∆∆∆∆∆ TEsting for new date technique

for line in dataFile:
    line = line.strip()
    lineList = line.split(",") #comma separate value; get the: DateTime,Consumption,Production,Nuclear,Wind,Hydroelectric,Oil and Gas,Coal,Solar,Biomass
    #Now to turn the first thing into date and time
    (d1, t1) = lineList[0].split(" ")
    date2 = Date(d1)
    time2 = Time(t1)
    # print(d1 + " " + t1)

    # TEMPORARY∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆
    if(date2.getStr() == "2019-01-02"): #For now, we dont want too much data so we're making it stop after the first day
        break


    #the key will be a tuple of the date and time, the value will be the energy data
    dataDict[(date2, time2)] = lineList[1:] #slice everything except for the date & time; (key = the date & time, value = the data)
   
    dateIndex[dIndex].append(date2) #can't use both because the index doesn't exist yet
    timeIndex[dIndex].append(time2)
    print( str(dIndex) + " " + str(tIndex)  )
    print(  dateIndex[dIndex][tIndex].getStr() + " " +  timeIndex[dIndex][tIndex].getStr()  )
    print(date2.getStr())

    tIndex+=1

    # print(dataDict[(dateIndex[0][-1], timeIndex[0][-1])])
    #Idea: since it's already ordered by time, I don't need to sort it. I just need to find a way to easily store the time/date data
    # print(date2.getStr() + " " + dateIndex[dIndex][tIndex].getStr())

    '''
    if(tIndex>0 and not (dateIndex[dIndex][tIndex-1].getStr() == date2.getStr())): #reset the timeIndex every time we get to a new day
        print("newday. dIndex:" + str(dIndex) + " tIndex:" + str(tIndex))
        print(dateIndex[dIndex][tIndex].getStr())
        print(dateIndex[dIndex][tIndex-1].getStr())
    '''

    if(tIndex>=24): #reset the timeIndex every time we get to a new day
        print("newday. dIndex:" + str(dIndex) + " tIndex:" + str(tIndex))
        # print(dateIndex[dIndex][tIndex].getStr())
        print(dateIndex[dIndex][tIndex-1].getStr())

        dIndex+=1
        dateIndex.append([date2])
        timeIndex.append([time2])
        tIndex=0   



   
    # dIndex+=1
    # dateIndex[dIndex][tIndex] = date2
    # timeIndex[dIndex][tIndex] = time2

    #                           ∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆ for somereason, it's starting a new day every time it gets to 2
    # print(dateIndex[dIndex][tIndex-1] + " " + d1)
    # print(d1 + " " + t1)
    # print(str(dIndex) + " " + str(tIndex))



# print(dateIndex[1][23])


#https://docs.bokeh.org/en/2.4.3/docs/gallery/bar_stacked.html Stacked Vbar for the graph of energy sources
#for the energy demand vs Supply, use a regular bar chrat
    

# for d in dataDict: #Test to see if I'm collecting data properly – victory! (just needed to cast the stuff to a list in the initialization)
#     # print(d.str)
#     print(str(d[0].dataList) + " " + str(d[1].dataList) + " " + str(dataDict[d]))



#Start off simple, Try to create a basic energy demand and supply graph
#Line graph with energy demand and supply 


#CREATE x and y lists for lines

# consLineXcoord = 0
energyConsFig = figure(width = 1000, title = "Energy Consumption vs. Time", x_axis_label = "Time", y_axis_label = "Energy (MegaWatts)")

energyConsFig.line((0, 0), (0, 10000)) #Yaxis
energyConsFig.line((0, 10000), (0, 0)) #Xaxis

# print("ONTO line")
# print (  dataDict[(dateIndex[0][0], timeIndex[0][0])]  )

print("DEBUGGING timeindex!")
print(len(timeIndex))
for i in range(len(timeIndex)):
    for j in range(len(timeIndex[i])):
        print(str(i) + " " + str(j))
        print(timeIndex[i][j].getStr())


# '''
print("starting Line")
for i in range(len(dateIndex)): #lets just go with the first day for now – date =0, time stops from 0-23
    consLineX = []
    consLineY = []
    consLineFinalCoord = ""

    prodLineX = []
    prodLineY = []
    prodLineFinalCoord = ""


    

    for j in range(len(dateIndex[i])): #consumption is the first value in the list
        # print(str(i) + " " + str(j) + " " + dateIndex[i][j].getStr())

        currentXCoord = (i*23 + j) * (10000/23)

        consumpPoint = dataDict[(dateIndex[i][j], timeIndex[i][j])][0] 
        consLineX.append(currentXCoord) #X values, for now it's a 1-1 thing
        consLineY.append(consumpPoint)
        consLineFinalCoord = int(consumpPoint)

        prodPoint = dataDict[(dateIndex[i][j], timeIndex[i][j])][1]
        prodLineX.append(currentXCoord) 
        prodLineY.append(prodPoint)     
        prodLineFinalCoord = int(prodPoint)
   

        energyConsFig.line((currentXCoord, currentXCoord), (0, -100), color = "black", line_width = 3)
        energyConsFig.text(x = currentXCoord-100, y = -500, text = [timeIndex[i][j].getStr()], text_font_size = "7px")

        # print(i*24 + j)
        # print(consumpPoint)
    col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    energyConsFig.line(consLineX, consLineY, line_width = 2, color = col)
    energyConsFig.text( x = 10000, y = consLineFinalCoord, text = ["Energy Consumption"], text_font_size = "7px")

    #for Production
    energyConsFig.line(prodLineX, prodLineY, line_width = 2, color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    energyConsFig.text(x = 10000, y= prodLineFinalCoord, text = ["Energy Production"], text_font_size = "7px")

show(energyConsFig)
# '''
        