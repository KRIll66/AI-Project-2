import math, random, copy, util

class SimAnneal(object):

    def __init__(self, grid):
    
        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.start_tour = grid.startingTour
        self.best_tour = copy.deepcopy(self.start_tour)
        self.curr_tour = grid.startingTour
        self.curr_cost = util.getTourCost( self.curr_tour, grid.costGraph)
        self.T = math.sqrt(self.grid.numCities) 
        self.stopping_temperature = 1e-8 
        self.best_cost = float("Inf")
        self.tour_list = []
        self.alpha = 0.995 
        self.stopping_iter = 1e6 
        self.iteration = 1

    # Simulated Annealing core algorithm
    def anneal(self):

        temp_thing = self.curr_tour

        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            temp_thing = self.swap(temp_thing)
            self.accept(temp_thing)
            self.T *= self.alpha
            self.iteration += 1
            
    def swap(self, tour):
        
        #choose to random cities
        city1 = random.randint(1, len(tour)-1)
        city2 = random.randint(1, len(tour)-1)
        #print(city1)
        #print(city2)
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
                self.best_cost, self.best_solution = candidate_cost, candidate
                
        else:
            if random.random() < self.p_accept(candidate_cost):
                self.curr_cost, self.curr_tour = candidate_cost, candidate
                self.tour_list.append(candidate)

