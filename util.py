import copy

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


# generates all possible child states from a parent state passed in and returns them as a list
# note that each child tour only differs from the parent state by 1 swap
# (i.e. two cities have switched places)
def getListOfTours(tourlist):
    i = 0
    first_city = tourlist[0]
    tourlist.remove(0)
    child_tours = []
    arr = []
    while i < len(tourlist) - 1:
        j = i + 1
        while j < len(tourlist):
            arr2 = copy.deepcopy(arr)
            arr2 = swap(tourlist, i, j)
            arr2.insert(0, first_city)
            child_tours.append(arr2)
            print(child_tours)
            j = j + 1
            arr.clear()
        i = i + 1
    child_tours.remove(0)
    return child_tours


# makes a deepcopy of a list and then swaps the two items at that list in index i and j
# returns the deepcopy of the list, which has the two items swapped
# original list passed in remains unaltered
def swap(list, i, j):
    templist = copy.deepcopy(list)
    templist[i], templist[j] = templist[j], templist[i]
    return templist














