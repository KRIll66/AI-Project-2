from math import cos
import grid, util


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
    
    tour1 = myGrid.getRandomTour()
    print (tour1)
    

    tour_1_cost = util.getTourCost(tour1, cost_graph)
    print ("Tour 1 cost:", tour_1_cost)
    
if __name__=='__main__':
        main()