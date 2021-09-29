from util import *
from grid import *


class HillClimbing:

    def __init__(self, grid):

        # we set best_config to startconfig because technically start_config is
        # our best state at the moment
        self.grid = grid
        self.best_tour = grid.startingTour
        self.start_tour = grid.startingTour

    # This method uses the hill-climbing algorithm to (try) find better tours than the one it starts with
    # It returns when it reaches a maximum or a plateau
    # If a better tour is found than the current better tour (stored in self.best_tour), then self.best_tour
    # will be updated to this new best_tour.
    # Note that self.best_tour may not be updated every time this method is called, since the maximum/plateau
    # found in a run might not be better than the maximum/plateau found in other runs
    def calculateBestTour(self):
        current_tour = self.start_tour

        while True:
            temp = current_tour

            # gets all child states from current config
            # (each child state is the current state with 2 cities swapped)
            child_tours = swap(current_tour)

            # if any child state is better than the current state, we replace the
            # current state with that child state
            for tour in child_tours:
                if getTourCost(tour, tour.costGraph) < getTourCost(current_tour, current_tour.costGraph):
                    current_tour = tour
                    # update the best tour
                    self.best_tour = current_tour

            # if current_state is the same as temp, we know it hasn't changed (i.e. it wasn't
            # replaced with one of its child states. This means we are at a maximum or plateau
            # so we exit the loop
            if current_tour == temp:
                break;

    # sets the start tour to whatever is passed in
    def setStartTour(self, tour):
        self.start_tour = tour

    # This method runs the hill climbing algorithm using random restart
    # Each time it "randomly restarts" the algorithm, it gives it random new start tour in hopes
    # of finding a better solution than the one already found
    def randomRestart(self, num_restarts):

        # does initial run, which calculates the best_tour
        self.calculateBestTour()

        i = 0
        # loops as many times as specified by num_restarts (minus one because of the initial run)
        while i < num_restarts - 1:
            # get a random start tour (note: may be one we've already done,
            # due to the nature of the hill climbing algorithm we don't know and don't care
            random_tour = grid.getRandomTour()

            # set the starting tour to the one we randomly just got
            self.setStartTour(random_tour)

            # calculate the best tour from the start tour
            self.calculateBestTour()

    def getBestTour(self):
        return self.best_tour
