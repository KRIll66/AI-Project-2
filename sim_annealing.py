
import math, random, copy, util
##################################################################################################
#
# sim_annealing.py
#
# This class is the simulated annealing algorithm for a travelling salesman person problem.
# This class relies on the data structures defined in the grid.py class and the helper functions in util.py
#
# A SimAnneal object is contains a contains a copy of a grid.
# nodelist helper function:
#       - purgelist(self) - clears data in openlist, cache, and closedlist. 
#
# Openlist is a list of unvisited Nodes that stored as a 3-tuple, (node, priority, count)  in a heapq. Priority is used for GBFS and A*, and count is used to ensure FIFO operation for identical priorities.
# openlist helper functions:
#       - push_to_openL(self, child_node, priority, count) - pushes node object "child_node" onto the openlist
#       - pop_openL(self) - removes and returns node at the top of the openlist
# 
# Closed, (or visited), nodes are nodes with a unique hash value that are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# ***attention*** Nodes that are visisted but do not have a unique hash are NOT stored in closedlist. Those nonunique nodes are to be stored in the cache.
# closedlist has helper functions: 
#       - push_to_closedL(self, node) - pushed node onto closedlist
#       - closedL_contains(self, hash) - checks if closedlist contains a node with matching hash value
#       - print_closedL(self, goal_state_tble) - prints list of all node state tables in closedlist
#
# Cache, stores all nodes in the search, (i.e visted and nonvisted that are created during the search), with a unique hash value that are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# cache has helper functions: 
#       - push_to_cache(self, node) - pushed node onto cache
#       - cache_contains(self, hash) - checks if cache contains a node with matching hash value
#
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

    # Simulated Annealing core algorithm
    def anneal(self):

        temp_thing = self.curr_tour
        
        while self.T >= self.stopping_temperature : #and self.iteration < self.stopping_iter:
            temp_thing = self.swap(temp_thing)           
            self.accept(temp_thing)
            self.T *= self.alpha
            self.iteration += 1
            
    def swap(self, tour):
        
        #choose to random cities
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
            if candidate_cost < self.best_cost:
                self.best_cost, self.best_tour = candidate_cost, candidate
                
        else:
            if random.random() < self.p_accept(candidate_cost):
                self.curr_cost, self.curr_tour = candidate_cost, candidate
                self.tour_list.append(candidate)

