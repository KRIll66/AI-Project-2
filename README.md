# AI-Project-2
CSCE A405 Assignment 2
Due Date: Tuesday, October 5, 2021, at 11:59 PM

Purpose: The goal of this assignment is to gain an understanding of iterative improvement algorithms commonly used to find optimal solutions in a wide variety of problem domains.

Background: Consider the dilemma of Traveling Salespersons. Starting from their home city, their task is to visit every city on a specified tour exactly once and return to their home city, while minimizing the total cost of the tour. Cost can be measured in several ways (total time, total distance traveled, etc.), but for our purposes lets assume that our salespeople are trying to minimize the total travel budget expended on the tour. As a master computer scientist and/or computer engineer, your job is to develop a computer program that reads a list of current airfares for direct one-way flights between pairs of cities, and uses an iterative improvement algorithm to identify the least-cost tour.

Requirements: For this assignment, you are required to solve the Traveling Salesperson Problem using each of the following iterative improvement algorithms:

a.	Hill-Climbing with Random Restart (R&N pp. 122-125)
b.	Simulated Annealing (R&N p. 125)

Your program should randomly generate an initial tour. It should then attempt to identify an optimized (least-cost) solution by independently utilizing each of the algorithms specified above.
To test your program for a graph containing N cities, create an N-by-N array of integers. Then initialize each array entry [J, K] to a randomly generated value between $100 and $2500 that represents the cost of flying (one-way) from city J to city K. Thoroughly debug your program(s). When you are satisfied that your software works, create five different randomly generated cost graphs, each of which contains 10 or more cities. For each iterative improvement algorithm, run your program five times for each graph, using a different randomly created tour as the starting configuration for each run. Measure the search cost and estimate the quality (optimality) of each of your solutions, and tabulate or graph your results from each iterative improvement algorithm in an appropriate manner.
Submit the following items as a compressed, zipped folder attached to an email:
a)	Your source code file(s).
b)	A report describing each of the following items:
1.	A brief description of how you adapted the generic hill-climbing with random restart and simulated annealing algorithms to solve the TSP.
2.	A table of your test results over the 25 runs.
3.	A summary of these results that compares and contrasts the overall performance of each algorithm.
I will test your program interactively, read your report, and send your grade with appropriate comments via electronic mail.

Your program should be written in a high-level language such as Python, Java, or C/C++.

Work in teams of one to three students on both the program and the report. Clearly identify the name and preferred email address of each team member at the top of your report. Do not copy any part of the code, test results, or report written by another group. Generic hill-climbing or simulated annealing code downloaded from the Internet, copied from a journal, or obtained from an external source may be used as part of your solution if and only if you give explicit credit to the original author(s) in your report. Since this project requires a considerable amount of data collection, I strongly suggest getting an early start!
