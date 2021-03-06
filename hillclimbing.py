from util import *
from grid import *


class HillClimbing:

    def __init__(self, grid):

        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.best_tour = grid.startingTour
        self.best_cost = getTourCost(grid.startingTour, grid.costGraph)
        self.better_tour = grid.startingTour
        self.start_tour = grid.startingTour
        self.cost_graph = grid.costGraph
        self.num_children = 0


    #reset hillclimbing attributes for the next run
    def reset (self):
        self.best_tour = self.grid.startingTour
        self.best_cost = getTourCost(self.grid.startingTour, self.grid.costGraph)
        self.better_tour = self.grid.startingTour
        self.start_tour = self.grid.startingTour
        self.num_children = 0


    # This method uses the hill-climbing algorithm to (try) find better tours than the one it starts with
    # It returns when it reaches a maximum or a plateau
    # If a better tour is found than the current better tour (stored in self.best_tour), then self.best_tour
    # will be updated to this new best_tour.
    # Note that self.best_tour may not be updated every time this method is called, since the maximum/plateau
    # found in a run might not be better than the maximum/plateau found in other runs
    def calculateBestTour(self):

        # copy the current start tour into current_tour
        current_tour = copy.deepcopy(self.start_tour)
        #print("current tour: ", current_tour)

        while True:
            cost = getTourCost(current_tour, self.cost_graph)
            #print("cost: ", cost)

            # gets all child states from current config
            # (each child state is the current state with 2 cities swapped)
            child_tours = getChildTours(current_tour)

            # if any child state is better than the current state, we replace the
            # current state with that child state
            for tour in child_tours:
                self.num_children+=1
                #print("child tour: ", tour)
                if getTourCost(tour, self.cost_graph) < getTourCost(current_tour, self.cost_graph):
                    current_tour = copy.deepcopy(tour)
                    #print("current tour", current_tour)

            # if current_state cost is the same as the cost we recording at the beginning of the loop,
            # we know current_state hasn't changed (i.e. it wasn't replaced with one of its child states)
            # This means we are at a maximum or plateau so we exit the loop
            if getTourCost(current_tour, self.cost_graph) == cost:
                # update the best tour adn best tour cost if this is a new best result
                if getTourCost(current_tour, self.cost_graph) < self.best_cost:
                    self.best_tour = copy.deepcopy(current_tour)
                    self.best_cost = getTourCost(current_tour, self.cost_graph)
                #update the better tour for this search iteration
                self.better_tour = copy.deepcopy(current_tour)
                break

    # sets the start tour to whatever is passed in
    def setStartTour(self, tour):
        self.start_tour = copy.deepcopy(tour)

    # This method runs the hill climbing algorithm using random restart
    # Each time it "randomly restarts" the algorithm, it gives it random new start tour in hopes
    # of finding a better solution than the one already found
    def randomRestart(self, cuttoff):

        
        num_restarts = 0 
        # does initial run, which calculates the best_tour
        self.calculateBestTour()
        #print ("The current iteration found that the better tour would be: ", self.better_tour, " with a cost of: ", getTourCost(self.better_tour, self.cost_graph),'\n')
        i = 0
        # loops as many times as specified by num_restarts (minus one because of the initial run)
        while num_restarts < cuttoff:
            # get a random start tour (note: may be one we've already done,
            # due to the nature of the hill climbing algorithm we don't know and don't care
            random_tour = self.grid.getRandomTour()

            # set the starting tour to the one we randomly just got
            self.setStartTour(random_tour)
           # print("The new random starting tour is: ", self.start_tour, " with a cost of: ", getTourCost(self.start_tour, self.cost_graph))
            # calculate the best tour from the start tour
            self.calculateBestTour()
            #print ("The current iteration found that the better tour would be: ", self.better_tour, " with a cost of: ", getTourCost(self.better_tour, self.cost_graph),'\n')
            #decrement restart count
            num_restarts+=1
       

    def getBestTour(self):
        return self.best_tour

    
