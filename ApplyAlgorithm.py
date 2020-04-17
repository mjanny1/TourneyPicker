#!/usr/local/bin/python3

import json

"""
main()
    current: The instance of the NewTourney class that is using this.
             NewTourney class can be found in BracketSolver.py

This function will return a 1 if Team 1 wins and will return
a 2 if Team 2 wins
"""

def main(current):
    return_value = Chalk(current.team1_seed, current.team2_seed)
    return return_value


"""



ALGORITHMS LISTED BELOW



"""

"""
Chalk: Solves the bracket based on chalk outcomes
"""
def Chalk(team1_seed, team2_seed):
    if team1_seed > team2_seed:
        return 2
    else:
        return 1


