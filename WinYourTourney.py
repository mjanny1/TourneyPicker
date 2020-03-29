#!/usr/local/bin/python3

import json
import collections
import ApplyAlgorithm as applyAlgorithm
import PrintBracket as printBracket

"""
Initializing Static Variables
"""
quadrants=collections.deque(["UpperLeft","BottomLeft","UpperRight","BottomRight"])
seeding=collections.deque([15,2,10,7,14,3,11,6,13,4,12,5,9,8,16,1])
seeds_remaining = collections.deque([])
final_4_seeds = collections.deque([])
round_of_64  = collections.deque([])
round_of_32  = collections.deque([])
sweet16      = collections.deque([])
elite8       = collections.deque([])
final4       = collections.deque([])
championship = collections.deque([])
class Tourney:
    champion = ""


"""
SolveRegion()
    region_name: Name of the region in the config file

Description:
    This will solve a single region based on the current
    algorithm set
"""
def SolveRegion(region_name, Round):
    print("Solving " + str(region_name) + " Region")
    seeds_remaining.clear()
    seeds_remaining.extend(seeding)
    seeds_in_the_next_round = collections.deque([])
    #While teams in the region still remain..
    while len(seeds_remaining) > 1:
        #Take the two teams next in the queue
        team1_seed = seeds_remaining.pop()
        team1_key = KeyBuilder(team1_seed, Round)
        team2_seed = seeds_remaining.pop()
        team2_key = KeyBuilder(team2_seed, Round)

        #Apply the Algorithm! (Returns a 1 or 2)
        winner = applyAlgorithm.main(region_name,
                                     team1_seed,
                                     team1_key,
                                     region_name,
                                     team2_seed,
                                     team2_key,
                                     Round)

        #Advance the Winner
        if winner == 1:
            seeds_in_the_next_round.appendleft(team1_seed)
            RecordWinner(Round, (data[region_name][team1_key[0]]["TeamName"]))
            lastSeed = team1_seed
        elif winner == 2:
            seeds_in_the_next_round.appendleft(team2_seed)
            RecordWinner(Round, (data[region_name][team1_key[0]]["TeamName"]))
            lastSeed = team2_seed
        else:
            print ("Error Occurred: Algorithm returned a value not equal to 1 or 2")
            print ("Algorithm returned: " + str(winner))
            break

        #See if the Round is complete
        if len(seeds_remaining) < 1:
            #Move on to the next round
            seeds_remaining.extend(seeds_in_the_next_round)
            seeds_in_the_next_round.clear() 
            Round = Round + 1

    #Save off winner's config reference for Final Four Processing
    final_4_seeds.appendleft(lastSeed)

def SolveFinalFour():
    # Check to make sure there are 4 teams
    if len(final_4_seeds) == 4:
        print("Solving Final Four")
        Round = 5
        #Maintain a list of the remaining regions
        regions_left = collections.deque([])
        regions_left.extend(quadrants)
        regions_left.rotate()
        championship_team_region = collections.deque([])
        #Maintain a list of the remaining seeds
        seeds_in_the_next_round = collections.deque([])
        #While teams in the region still remain..
        while len(final_4_seeds) > 1:
            #Take the two teams next in the queue
            team1_region = regions_left.pop()
            team1_seed = final_4_seeds.pop()
            team1_key = KeyBuilder(team1_seed, Round)
            team2_region = regions_left.pop()
            team2_seed = final_4_seeds.pop()
            team2_key = KeyBuilder(team2_seed, Round)

            #Apply the Algorithm! (Returns a 1 or 2)
            winner = applyAlgorithm.main(team1_region,
                                         team1_seed,
                                         team1_key,
                                         team2_region,
                                         team2_seed,
                                         team2_key,
                                         Round)

            #Advance the Winner
            if winner == 1:
                seeds_in_the_next_round.appendleft(team1_seed)
                championship_team_region.appendleft(team1_region)
                RecordWinner(Round, (data[team1_region][team1_key[0]]["TeamName"]))
                print(data[team1_region][team1_key[0]]["TeamName"])
            elif winner == 2:
                seeds_in_the_next_round.appendleft(team2_seed)
                championship_team_region.appendleft(team2_region)
                RecordWinner(Round, (data[team2_region][team2_key[0]]["TeamName"]))
                print(data[team2_region][team2_key[0]]["TeamName"])
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
                Round = Round + 1



def RecordWinner(Round, team_name):
    if Round == 1:
        round_of_32.appendleft(team_name)
        #print (round_of_32)
    elif Round == 2:
        sweet16.appendleft(team_name)
        #print (sweet16)
    elif Round == 3:
        elite8.appendleft(team_name)
        #print (elite8)
    elif Round == 4:
        final4.appendleft(team_name)
        #print (final4)
    elif Round == 5:
        championship.appendleft(team_name)
        #print (championship)
    elif Round == 6:
        Tourney.champion = team_name
        #print (Tourneychampion)
    else:
        print ("ERROR Occurred while recording winner: " + str(team_name))


def KeyBuilder(seed, Round):
    seed_key =            str(seed) + "-Seed"
    win_pct_key =  "R" + str(Round) + "_Win_Pct"
    pick_pct_key = "R" + str(Round) + "_Pick_Pct"
    keys = [seed_key, win_pct_key, pick_pct_key]
    return keys

def GetRoundOf64():
    for x in range(0,len(quadrants)):
        for y in range(15, -1, -1):
            key = str(seeding[y]) + "-Seed"
            round_of_64.appendleft(data[quadrants[x]][key]["TeamName"])

#try:
with open("./config/bracket.json") as json_file:
    data = json.load(json_file)
    #print (data["UpperLeft"]["1-Seed"]["TeamName"])
    #print (data[quadrants[0]]["2-Seed"]["TeamName"])
    for n in range(0,len(quadrants)):
        SolveRegion(quadrants[n], 1)
    SolveFinalFour()
    print ("After Final Four champion: " + str(Tourney.champion))
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
                      Tourney.champion)
#except:
#    print("Error Reading Config File!")

