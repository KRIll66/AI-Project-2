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

# returns a list of tours
def swap(tour):
    list_of_tours = []


