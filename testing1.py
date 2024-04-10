# from bokeh import figure, show, gridplot

#Removed from Line1: DateTime,Consumption,Production,Nuclear,Wind,Hydroelectric,Oil and Gas,Coal,Solar,Biomass



class Date:
    # self.str, self.dataList
    def __init__(self, s):
        self.str = s
        self.dataList = list(s.split("-"))#REMINDER: You gotta cast this to a list!!

    # def print(self):
    #     return self.dataList

        
class Time:
    # self.str, self.dataList
    def __init__(self, s):
        self.str = s
        self.dataList = list(s.split(":")) #hour, minute, second
    def getHour(self):
        return self.dataList[0]
    # def print(self):
    #     return self.dataList


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
for line in dataFile:
    line = line.strip()
    lineList = line.split(",") #comma separate value; get the: DateTime,Consumption,Production,Nuclear,Wind,Hydroelectric,Oil and Gas,Coal,Solar,Biomass
    #Now to turn the first thing into date and time
    (d1, t1) = lineList[0].split(" ")
    date2 = Date(d1)
    time2 = Time(t1)
    # print(d1 + " " + t1)

    #the key will be a tuple of the date and time, the value will be the energy data
    dataDict[(date2, time2)] = lineList[1:] #slice everything except for the date & time; (key = the date & time, value = the data)

    #Idea: since it's already ordered by time, I don't need to sort it. I just need to find a way to easily store the time/date data

    if(tIndex>0 and (not dateIndex[dIndex][tIndex-1].str == date2.str)): #reset the timeIndex every time we get to a new day
        print("newday")
        dIndex+=1
        dateIndex.append([d1])
        timeIndex.append([d1])
        tIndex=0   


    dateIndex[dIndex].append(date2)
    timeIndex[dIndex].append(time2)
   
    # dIndex+=1
    tIndex+=1
    # dateIndex[dIndex][tIndex] = date2
    # timeIndex[dIndex][tIndex] = time2

    #                           ∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆ for somereason, it's starting a new day every time it gets to 2
    # print(dateIndex[dIndex][tIndex-1] + " " + d1)
    print(d1 + " " + t1)
    print(str(dIndex) + " " + str(tIndex))

    #TEMPORARY
    if(date2.str == "2019-01-02"): #For now, we dont want too much data so we're making it stop after the first day
        break

#https://docs.bokeh.org/en/2.4.3/docs/gallery/bar_stacked.html Stacked Vbar for the graph of energy sources
#for the energy demand vs Supply, use a regular bar chrat
    

# for d in dataDict: #Test to see if I'm collecting data properly – victory! (just needed to cast the stuff to a list in the initialization)
#     # print(d.str)
#     print(str(d[0].dataList) + " " + str(d[1].dataList) + " " + str(dataDict[d]))


# print(dataDict[("2019-01-01","00:00:00")])

#Start off simple, Try to create a basic energy demand and supply graph
#Histogram with the time for a certain day at the bottom 
vBarSize = 10
# energyDemandFig = figure(width = 100)
for i in range(0): #lets just go with the first day for now – date =0, time stops from 0-23
    for j in range(23): #consumption is the first value in the list
        dataDict[(dateIndex[i], timeIndex[j])][0] 