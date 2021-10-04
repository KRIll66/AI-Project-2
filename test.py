from math import cos
import grid
import hillclimbing
from util import *


#################################################
#The return of test.py!!! 
#Add whatever you'd like to test funcitonality
#
#################################################



def main():
    
    #myGrid is a grid object
    myGrid = grid.Grid(4)         
    myGrid.setGrid()
    myGrid.displayGrid()
    #cost_graph has the grid of flight costs
    cost_graph = myGrid.getGrid()
    
    tour1 = myGrid.getRandomTour()
    print(tour1)
    tour2 = myGrid.getRandomTour()
    print (tour2)    

    tour_1_cost = getTourCost(tour1, cost_graph)
    print ("Tour 1 cost:", tour_1_cost)  

    myGrid.startingTour = tour1
    
    hc = hillclimbing.HillClimbing(myGrid)
    print("start tour", hc.start_tour)
    hc.calculateBestTour()
    print("better tour", hc.best_tour)






    
if __name__=='__main__':
        main()