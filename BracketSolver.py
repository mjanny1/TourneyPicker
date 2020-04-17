#!/usr/local/bin/python3

import json
import collections
import ApplyAlgorithm as applyAlgorithm
import PrintBracket as printBracket

"""
Initializing Static Variables
"""
quadrants=collections.deque(["East","West","South","Midwest"])
seeding=collections.deque([15,2,10,7,14,3,11,6,13,4,12,5,9,8,16,1])
seeds_remaining = collections.deque([])
final_4_seeds = collections.deque([])
round_of_64  = collections.deque([])
round_of_32  = collections.deque([])
sweet16      = collections.deque([])
elite8       = collections.deque([])
final4       = collections.deque([])
championship = collections.deque([])

"""
Class: NewTourney

    Params:
        year: Year of the tournament
        data: Data from the config.json file loaded

    Description: This creates a new tournament instance which for that year

"""
class NewTourney:
    def __init__(self, year, data):
        self.data            = data
        self.year            = year
        self.round           = 1
        self.champion        = ""
        self.team1_name      = ""
        self.team1_region    = ""
        self.team1_seed      = 0
        self.team1_vegas_pct = 0
        self.team1_pick_pct  = 0
        self.team2_name      = ""
        self.team2_region    = ""
        self.team2_seed      = 0
        self.team2_vegas_pct = 0
        self.team2_pick_pct  = 0

    def set_team1(self, region_name, seed):
        self.team1_region    = region_name
        self.team1_seed      = seed
        team1_key            = KeyBuilder(seed, self.round)
        self.team1_name      = data[region_name][team1_key[0]]["TeamName"]
        self.team1_vegas_pct = data[self.team1_region][team1_key[0]][team1_key[1]]
        self.team1_pick_pct  = data[self.team1_region][team1_key[0]][team1_key[2]]

    def set_team2(self, region_name, seed):
        self.team2_region    = region_name
        self.team2_seed      = seed
        team2_key            = KeyBuilder(seed, self.round)
        self.team2_name      = data[region_name][team2_key[0]]["TeamName"]
        self.team2_vegas_pct = data[self.team2_region][team2_key[0]][team2_key[1]]
        self.team2_pick_pct  = data[self.team2_region][team2_key[0]][team2_key[2]]

    def increment_round(self):
        self.round = self.round + 1

"""
SolveRegion()
    region_name: Name of the region in the config file

Description:
    This will solve a single region based on the current
    algorithm set
"""
def SolveRegion(region_name, current):
    print("Solving " + str(region_name) + " Region")
    current.round = 1
    seeds_remaining.clear()
    seeds_remaining.extend(seeding)
    seeds_in_the_next_round = collections.deque([])
    #While teams in the region still remain..
    while len(seeds_remaining) > 1:
        #Take the two teams next in the queue
        current.team1_seed = seeds_remaining.pop()
        current.team2_seed = seeds_remaining.pop()

        #Set the Current Teams for Algorithm Use
        current.set_team1(region_name, current.team1_seed)
        current.set_team2(region_name, current.team2_seed)

        #Apply the Algorithm! (Returns a 1 or 2)
        winner = applyAlgorithm.main(current)

        #Advance the Winner
        if winner == 1:
            seeds_in_the_next_round.appendleft(current.team1_seed)
            RecordWinner(current, current.team1_name)
            lastSeed = current.team1_seed
        elif winner == 2:
            seeds_in_the_next_round.appendleft(current.team2_seed)
            RecordWinner(current, current.team2_name)
            lastSeed = current.team2_seed
        else:
            print ("Error Occurred: Algorithm returned a value not equal to 1 or 2")
            print ("Algorithm returned: " + str(winner))
            break

        #See if the Round is complete
        if len(seeds_remaining) < 1:
            #Move on to the next round
            seeds_remaining.extend(seeds_in_the_next_round)
            seeds_in_the_next_round.clear() 
            current.increment_round()

    #Save off winner's config reference for Final Four Processing
    final_4_seeds.appendleft(lastSeed)

"""
SolveFinalFour()

Description:
    This will solve the Final Four.
"""
def SolveFinalFour(current):
    # Check to make sure there are 4 teams
    if len(final_4_seeds) == 4:
        print("Solving Final Four")
        current.round = 5
        #Maintain a list of the remaining regions
        regions_left = collections.deque([])
        regions_left.extend(quadrants)
        regions_left.reverse()
        championship_team_region = collections.deque([])
        #Maintain a list of the remaining seeds
        seeds_in_the_next_round = collections.deque([])
        #While teams in the region still remain..
        while len(final_4_seeds) > 1:
            #Take the two teams next in the queue
            current.team1_seed = final_4_seeds.pop()
            current.team2_seed = final_4_seeds.pop()

            #Set the Current Teams for Algorithm Use
            current.set_team1(regions_left.pop(), current.team1_seed)
            current.set_team2(regions_left.pop(), current.team2_seed)

            #Apply the Algorithm! (Returns a 1 or 2)
            winner = applyAlgorithm.main(current)

            #Advance the Winner
            if winner == 1:
                seeds_in_the_next_round.appendleft(current.team1_seed)
                championship_team_region.appendleft(current.team1_region)
                RecordWinner(current, current.team1_name)
            elif winner == 2:
                seeds_in_the_next_round.appendleft(current.team2_seed)
                championship_team_region.appendleft(current.team2_region)
                RecordWinner(current, current.team2_name)
            else:
                print ("Error Occurred: Algorithm returned a value not equal to 1 or 2")
                print ("Algorithm returned: " + str(winner))
                break

            #See if the Round is complete
            if len(final_4_seeds) < 1:
                #Move on to the next round
                final_4_seeds.extend(seeds_in_the_next_round)
                regions_left.extend(championship_team_region)
                seeds_in_the_next_round.clear() 
                current.increment_round()

"""
RecordWinner()
    team_name: The name of the team that just won.

Description:
    This will the record the winner in a queue for each round.
"""
def RecordWinner(current, team_name):
    if current.round == 1:
        round_of_32.appendleft(team_name)
        #print (round_of_32)
    elif current.round == 2:
        sweet16.appendleft(team_name)
        #print (sweet16)
    elif current.round == 3:
        elite8.appendleft(team_name)
        #print (elite8)
    elif current.round == 4:
        final4.appendleft(team_name)
        #print (final4)
    elif current.round == 5:
        championship.appendleft(team_name)
        #print (championship)
    elif current.round == 6:
        current.champion = team_name
        #print (Tourneychampion)
    else:
        print ("ERROR Occurred while recording winner: " + str(team_name))

"""
KeyBuilder()
    Round: The round you are currently solving

Description:
    This will return an index key to get values from the config file.
"""
def KeyBuilder(seed, Round):
    seed_key =            str(seed) + "-Seed"
    win_pct_key =  "R" + str(Round) + "_Win_Pct"
    pick_pct_key = "R" + str(Round) + "_Pick_Pct"
    keys = [seed_key, win_pct_key, pick_pct_key]
    return keys

"""
GerRoundOf64()

Description:
    This will create a queue of the teams in the Round of 64
"""
def GetRoundOf64():
    for x in range(0,len(quadrants)):
        for y in range(15, -1, -1):
            key = str(seeding[y]) + "-Seed"
            round_of_64.appendleft(data[quadrants[x]][key]["TeamName"])

with open("./config/config.json") as json_file:
    data = json.load(json_file)
    current = NewTourney(2019, data)
    for n in range(0,len(quadrants)):
        SolveRegion(quadrants[n], current)
    SolveFinalFour(current)
    region_list = collections.deque([])
    region_list.extend(quadrants)
    region_list.rotate()
    GetRoundOf64()
    printBracket.main(region_list,
                      round_of_64,
                      round_of_32,
                      sweet16,
                      elite8,
                      final4,
                      championship,
                      current.champion)

