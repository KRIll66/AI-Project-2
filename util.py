import grid

################################################################
#util.py
#This module hosts methods that will handle repetetive heavy lifting for the search algorithms
#the algorithms should be able to get all the outsied data and functionality that they need 
#from util.py
#
#global variables:
#cost_grid: a 2d array the represents the cost to travel from city to city
#
#getTourCost():
#gets the total cost for a tour of the cities, the search algorithms use this value
#to determine an effective move and to find local maxima
#
###############################################################


#calculate the cost for this tour, return cost as an integer
def getTourCost(tour, cost_graph):
    cost = 0
    
    for flight in tour:
        this_flight_cost = cost_graph[flight[0]][flight[1]]
        cost += this_flight_cost
    return cost

# Takes in a tour in (x, y) format and returns it as a list
# For example: (1, 2) (2, 3) (3, 4) (4, 1) would be converted to [1, 2, 3, 4]
def convertTourToList(tour):
    i = 0
    city_array = []
    while i < len(tour):
        temp = tour[i]
        city_array.append(temp[0])
        i = i + 1
    return city_array

# NOT working properly yet! Both loops only run once.
def swapListOfTours(tourlist):
    i = 0
    first_city = tourlist[0]
    tourlist.remove(0)
    child_tours = []
    while i < (len(tourlist) - 1):
        j = i + 1
        while j < len(tourlist):
            arr = swap(tourlist, i, j)
            print(arr)
            arr.insert(0, first_city)
            child_tours.append(arr)
            print(j)
            j = j + 1
            arr.clear()
        i = i + 1

    return child_tours

def swap(list, i, j):
    templist = list
    templist[i], templist[j] = templist[j], templist[i]
    return templist












