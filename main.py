from math import cos
import grid, util, sys


#################################################
#################################################



def main():
    user_input = 0
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

        #!!!!!!ENTER THE SEARCH ALGORITHM BELOW HERE!!!!!!
        city_tour.displayGrid()

        #!!!!!!ENTER THE SEARCH ALGORITHM ABOVE HERE!!!!!!

        #Exit protocol, if user is finished then sys.exit()
        user_input = input("Would you like to run the program again?, Enter 'Y' to continue or any other key to exit: ")
        if user_input is not 'Y' and user_input is not 'y': sys.exit()

if __name__=='__main__':
        main()