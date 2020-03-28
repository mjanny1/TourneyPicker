#!/usr/local/bin/python3

import json

"""
main()
    team1_seed: seed number
    team1_key:  team1 config keys
    team2_seed: seed number
    team2_key:  team2 config keys
    Round:      round number

This function will return a 1 if Team 1 wins and will return
a 2 if Team 2 wins
"""
def main(team1_region, team1_seed, team1_key, team2_region, team2_seed, team2_key, Round):
    if team1_seed < team2_seed:
        return 1
    else:
        return 2

