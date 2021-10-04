import math, random, copy, util

class SimAnneal(object):

    def __init__(self, grid):
    
        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.start_tour = grid.startingTour
        self.best_tour = copy.deepcopy(self.start_tour)
        self.curr_tour = self.grid.startingTour
        self.curr_cost = util.getTourCost(self.start_tour, self.grid.costGraph)
        self.T = math.sqrt(self.grid.numCities)# if self.T == -1 else self.T
        self.stopping_temperature = 1e-8# if self.stopping_temperature == -1 else self.stopping_temperature
        self.best_cost = float("Inf")
        self.tour_list = []
        self.alpha = 0.995# if self.alpha == -1 else self.alpha 
        self.stopping_iter = 1e6# if self.stopping_iter == -1 else self.stopping_iter
        self.iteration = 1

    # Simulated Annealing core algorithm
    def anneal(self):

        temp_thing = self.curr_tour
        #print ("Temp thing is: ", temp_thing)

        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            temp_thing = self.swap(temp_thing)
            #print ("Swapped temp thing is: ", temp_thing)
            self.accept(temp_thing)
            self.T *= self.alpha
            self.iteration += 1
            
        



    def swap(self, tour):
        
        #choose to random cities
        city1 = random.randint(1, len(tour)-1)
        city2 = random.randint(1, len(tour)-1)

        #swap cities in tour
        tour[city1], tour[city2] = tour[city2], tour[city1]
        
        #return modified tour
        return tour



    def p_accept(self, candidate_cost):

        return math.exp(-abs(candidate_cost - self.curr_cost) / self.T)

    def accept(self, candidate):

        candidate_cost = util.getTourCost(candidate, self.grid.costGraph)
        #print ("the current cost is: ", self.curr_cost, " and the candidate cost is: ", candidate_cost)
        if candidate_cost < self.curr_cost:
            self.curr_cost, self.curr_tour = candidate_cost, candidate
            self.tour_list.append(candidate)
            if candidate_cost < self.best_cost:
                self.best_cost, self.best_solution = candidate_cost, candidate
                
        else:
            if random.random() < self.p_accept(candidate_cost):
                self.curr_cost, self.curr_tour = candidate_cost, candidate
                self.tour_list.append(candidate)

