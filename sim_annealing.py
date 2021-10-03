import math, random, copy, util

class SimAnneal(object):

    def __init__(self, grid):
    
        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.start_tour = grid.startingTour
        self.best_tour = copy.deepcopy(self.start_tour)
        self.curr_tour = None
        self.T = math.sqrt(self.grid.num_cities) if self.T == -1 else self.T
        self.stopping_temperature = 1e-8 if self.stopping_temperature == -1 else self.stopping_temperature
        self.best_fitness = float("Inf")
        self.tour_list = []
        self.alpha = 0.995 if self.alpha == -1 else self.alpha 
        self.stopping_iter = 1e6 if self.stopping_iter == -1 else self.stopping_iter
        self.iteration = 1

    # Simulated Annealing core algorithm
    def anneal(self):

        curr_tour = self.start_tour
        
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            
            self.accept(curr_tour)
            self.T *= self.alpha
            self.iteration += 1
            self.tour_list.append(curr_tour)
        

        



    def swap(self, tour):
        
        #choose to random cities
        city1 = random.randint(1, len(tour)-2)
        city2 = random.randint(1, len(tour)-2)

        #swap cities in tour
        tour[city1], tour[city1+1], tour[city2], tour[city2+1] = tour[city2], tour[city2+1], tour[city1], tour[city1+1]
        
        #return modified tour
        return tour

"""


    def p_accept(self, candidate_fitness):
        """
        Probability of accepting if the candidate is worse than current.
        Depends on the current temperature and difference between candidate and current.
        """
        return math.exp(-abs(candidate_fitness - self.cur_fitness) / self.T)

    def accept(self, candidate):
        """
        Accept with probability 1 if candidate is better than current.
        Accept with probabilty p_accept(..) if candidate is worse.
        """
        candidate_fitness = self.fitness(candidate)
        if candidate_fitness < self.cur_fitness:
            self.cur_fitness, self.cur_solution = candidate_fitness, candidate
            if candidate_fitness < self.best_fitness:
                self.best_fitness, self.best_solution = candidate_fitness, candidate
        else:
            if random.random() < self.p_accept(candidate_fitness):
                self.cur_fitness, self.cur_solution = candidate_fitness, candidate"""

