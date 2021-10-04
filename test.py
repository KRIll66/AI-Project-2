from math import cos
import grid
import hillclimbing, sim_annealing
from util import *


#################################################
#The return of test.py!!! 
#Add whatever you'd like to test funcitonality
#
#################################################



def main():
    
    #myGrid is a grid object
    myGrid = grid.Grid(5)         
    myGrid.setGrid()
    myGrid.displayGrid()
    #cost_graph has the grid of flight costs
    cost_graph = myGrid.getGrid()
    
    #must set the original starting tour prior to calling search functions
    tour1 = myGrid.getRandomTour()    
    myGrid.startingTour = tour1

    anneal = sim_annealing.SimAnneal(myGrid)
    anneal.anneal()
    print ("simulated annealing best cost: ", anneal.best_cost)
    print ("sim annealing best state is: ", anneal.best_tour)

    hc = hillclimbing.HillClimbing(myGrid)   
    hc.randomRestart(5)

    print("best tour", hc.best_tour, "for cost of: ", getTourCost(hc.best_tour, cost_graph))






    
if __name__=='__main__':
        main()