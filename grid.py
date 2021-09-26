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
        for x in range(self.numCities) :
            for y in range(self.numCities):               
                #cannot fly from Anchorage to Anchorage
                if (x == y):
                    self.costGraph[x][y] = 0
                else:
                    self.costGraph[x][y] = random.randrange(100, 2500)


    #ensure every city gets visited only once, return the tour as a list of sets [(1,0), (0,3),...]
    def getRandomTour(self):
         
        city_list = []
        for i in range(self.numCities):
            city_list.append(i) 

        #remove home city and reinsert at beginning of randomized tour
        homeCity = city_list.pop(0)
        random.shuffle(city_list)       
        city_list.insert(0, homeCity)
        #return home at end our tour
        city_list.append(homeCity)

        #build list of cost grid coordinate sets (represents the tour)
        tour = []
        for i in range(len(city_list)):
            if i == len(city_list)-1:
                break
            tour.append((city_list[i], city_list[i+1]))
            
        return tour


    def getGrid(self):
        return self.costGraph


    def displayGrid (self):
        for row in self.costGraph:
            print (row)