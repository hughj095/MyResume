Multi-Armed Bandit Problem
Reinforcement Learning is used to move robots with a list of tasks, 
    or train the robot to walk with rules and a goal
The Multi Armed Bandit Problem is the name for a line of 
    slot machines (each with one arm) and the order of playing
    them in order to win and max your return.  Each has a 
    distribution of 7s and cherries that they pick to return.

Upper Confidence Bound is finding among all of the slot machines
    which machine has the best distribution of wins by testing each 
    machine.  The max and min "bound" refines or shrinks with each 
    measurement until it converges onto the average distribution,
    or the average win or loss.  Requires an update every round.

An example in business is to test for the most effective 
    marketing campaign ad.  The goal is to find the most effective
    while running the campaign, the quickest way possible.  Exploration
    and Exploitation at the same time.

Thompson Sampling also solves for multiple "arms".  It takes 3 samples of the distribution
    to determine the full distribution of the best "arm".  Using the data point samples, we can 
    estimate where the peaks of the distributions will be.  This is a Probalitic algorithm, where 
    UCB is a deterministic algorithm.  Can accomodate delayed feedback.  Better empirical evidence.





