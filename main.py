from math import cos, inf
import grid, util, sys, sim_annealing, hillclimbing


#################################################
#################################################



def main():
    user_input = 0
    #run random restart 100 times
    num_iterations = 100
    best_hc_tour = []
    best_hc_cost = inf
    best_sim_tour = []
    best_sim_cost = inf

    print("\nWelcome to the 'Traveling Salesman' route finding application\n")

    #outer loop runs as long as user chooses to keep entering city tours
    while True:
        
        #inner loop handles user input, ensures valid input type and value of cities
        #num_cities must be an integer greater than 1
        while True:
            user_input = input("To begin, select the number of cities you wish to vist: ")
            try:
                num_cities = int(user_input)
                if num_cities > 1:
                    break
                else:print("The number of cities must be greater than 1...\n")
            except ValueError:
                print("Error: user input must be an integer...\n")
        

        #city_tour is the grid object to pass to the search algorithm
        #setGrid is required to establish cost to travel from city to city
        city_tour = grid.Grid(num_cities)
        city_tour.setGrid()
        start_tour = city_tour.getRandomTour()
        city_tour.startingTour = start_tour
       
        #create search algorithm object
        anneal = sim_annealing.SimAnneal(city_tour)
        hc = hillclimbing.HillClimbing(city_tour)

        #run this cost graph 5 times for simulated annealing and 5 times for random restart
        for i in range (5):
            #run annealing for this start point
            anneal.anneal()
            #display this iterations results for simulatetd annealing
            print ("Round", i+1, "results for simulated annealing:")
            print ("Starting cost:", util.getTourCost(start_tour, city_tour.costGraph))
            print ("Best cost found:", anneal.best_cost)
            print ("Number of new states generated in this search:", anneal.iteration, "\n")


            #run hilllclimbing with random restart for this start point
            hc.randomRestart(num_iterations)
            #display this iterations results for hill climbing
            print ("Round", i+1, "results for hill climbing with random restart:")
            print ("Starting cost:", util.getTourCost(start_tour, city_tour.costGraph))
            print ("Best cost found:", hc.best_cost)
            print ("Number of new states generated in this search:", hc.num_children, "\n")
           
            if best_sim_cost > anneal.best_cost:
                best_sim_cost, best_sim_tour = anneal.best_cost, anneal.best_tour

            if best_hc_cost > hc.best_cost:
                best_hc_cost, best_hc_tour = hc.best_cost, hc.best_tour
           
            #reset search attributes for next run, get a new random start point
            anneal.reset()
            hc.reset()
            start_tour = city_tour.getRandomTour()
            city_tour.startingTour = start_tour       

        #display this runs results, compare best answer found
        print("The best tour found with Simulated Annealing is:", best_sim_tour, "with a cost of:", best_sim_cost)
        print("The best tour found with Hill Climbing is:      ", best_hc_tour, "with a cost of:", best_hc_cost)


        #Exit protocol, if user is finished then sys.exit()
        user_input = input("Would you like to run the program again?, Enter 'Y' to continue or any other key to exit: ")
        if user_input is not 'Y' and user_input is not 'y': sys.exit()
        else:
            #reset the best variables
            best_hc_tour = []
            best_hc_cost = inf
            best_sim_tour = []
            best_sim_cost = inf

if __name__=='__main__':
        main()