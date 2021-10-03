import random

#############################################################################
#Grid.py
#This is a class for building the cost grid and handling the random tour generations
#
#A grid project has a list of cities, a startingTour, and a cost graph 
#
#setGrid() randomly assigns costs to 'fly' from city to city, cannot fly from one city to itself
#
#getRandomTour() returns a random tour of the cities, this is needed to start the search 
#algortithms and any time a local maxima is found
#
#getGrid() returns the costGraph in case any other methods from other classes need that information
#
#displayGrid() displays the costGraph, this is for visual purposes only and may not be 
#necessary in the implementation of the final program
##############################################################################


class Grid:

    #constructor, only receives number of cities from main
    def __init__(self, numCities):
        self.costGraph = [[0 for i in range(numCities)] for j in range (numCities)]
        self.startingTour = [()]
        self.numCities = numCities

    
    #populates the costGraph with random costs
    def setGrid(self):
        for x in range(self.numCities):
            for y in range(self.numCities):               
                #cannot fly from Anchorage to Anchorage
                if (x == y):
                    self.costGraph[x][y] = 0
                else:
                    self.costGraph[x][y] = random.randrange(100, 2500)


    #takes the number of cities and generates a random tour of those cites
    #home city remains the home city always
    def getRandomTour(self):
         
        city_list = []
        for i in range(self.numCities):
            city_list.append(i)        
        print("Original City List: ", city_list)

        #remove home city, shuffle the other cities, then insert home city back
        #at the start of the list
        home_city = city_list.pop(0)
        random.shuffle(city_list)
        city_list.insert(0,home_city)

        print("Randomized City List: ", city_list)

        return city_list


    def getGrid(self):
        return self.costGraph


    def displayGrid (self):
        for row in self.costGraph:
            print(row)