
import math, random, copy, util
##################################################################################################
#
# sim_annealing.py
#
# This class is the simulated annealing algorithm for a travelling salesman person problem.
# This class relies on the data structures defined in the grid.py class and the helper functions in util.py
#
# A SimAnneal object is contains a contains a copy of a grid.
##################################################################################################
class SimAnneal(object):

    def __init__(self, grid):
    
        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.start_tour = grid.startingTour
        self.best_tour = copy.deepcopy(self.start_tour)
        self.curr_tour = self.grid.startingTour
        self.curr_cost = util.getTourCost(self.start_tour, self.grid.costGraph)
        self.T = math.sqrt(self.grid.numCities)
        self.stopping_temperature = 1e-200
        self.best_cost = float("Inf")
        self.tour_list = []
        self.alpha = 0.995
        self.stopping_iter = 1e10
        self.iteration = 1

    #resets applicable attributes between runs
    def reset (self):
        self.best_tour = copy.deepcopy(self.start_tour)
        self.curr_tour = self.grid.startingTour
        self.curr_cost = util.getTourCost(self.start_tour, self.grid.costGraph)
        self.best_cost = float("Inf")
        self.iteration = 1
        self.T = math.sqrt(self.grid.numCities)
        self.start_tour
        self.start_tour = self.grid.startingTour

    # Simulated Annealing core algorithm
    def anneal(self):

        temp_thing = self.curr_tour
        
        while self.T >= self.stopping_temperature : #and self.iteration < self.stopping_iter:
            temp_thing = self.swap(temp_thing)           
            self.accept(temp_thing)
            self.T *= self.alpha
            self.iteration += 1
            
    def swap(self, tour):
        
        #choose two random cities
        city1 = random.randint(1, len(tour)-1)
        city2 = random.randint(1, len(tour)-1)
        
        #swap cities in tour
        temp = copy.deepcopy(tour)
        temp[city1], temp[city2] = temp[city2], temp[city1]
        
        #return modified tour
        return temp


    
    def p_accept(self, candidate_cost):

        return math.exp(-abs(candidate_cost - self.curr_cost) / self.T)

    def accept(self, candidate):

        candidate_cost = util.getTourCost(candidate, self.grid.costGraph)
        
        if candidate_cost < self.curr_cost:
            self.curr_cost, self.curr_tour = candidate_cost, candidate
            self.tour_list.append(candidate)
            if candidate_cost <= self.best_cost:
                self.best_cost, self.best_tour = candidate_cost, candidate
                
        else:
            if random.random() < self.p_accept(candidate_cost):
                self.curr_cost, self.curr_tour = candidate_cost, candidate
                self.tour_list.append(candidate)

