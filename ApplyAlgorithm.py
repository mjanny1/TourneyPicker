#!/usr/local/bin/python3

import json
#import BracketSolver as bracketSolver

"""
main()
    team1_seed: seed number
    team1_key:  team1 config keys
    team2_seed: seed number
    team2_key:  team2 config keys
    Round:      round number

This function will return a 1 if Team 1 wins and will return
a 2 if Team 2 wins

Example of team1_key: ['1-Seed', 'R1_Win_Pct', 'R1_Pick_Pct']
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


