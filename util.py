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
#Change TourCost to receive a tour as a list (example lsit of [0-4] is [0,1,2,3,4])
#return cost as an integer
def getTourCost(tour, cost_graph):
    cost = 0
    
    #create list of coordinates for flight costs
    #add home city to end of tour list
    tour.append(tour[0])

    #build list of cost grid coordinate sets (represents the tour)
    tour_coordinates = []
    for i in range(len(tour)):
        if i == len(tour)-1:
            break
        tour_coordinates.append((tour[i], tour[i+1]))
    

    for flight in tour_coordinates:
        this_flight_cost = cost_graph[flight[0]][flight[1]]
        cost += this_flight_cost
    return cost




def swapListOfTours(tourlist):
    i = 0
    first_city = tourlist[0]
    tourlist.remove(0)
    child_tours = []
    while i < len(tourlist) - 1:
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
    print('i = ', i)
    print('j = ', j)
    templist = copy.deepcopy(list)
    templist[i], templist[j] = templist[j], templist[i]
    return templist












