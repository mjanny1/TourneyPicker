#!/usr/local/bin/python3

import json
import collections

"""
main()
    round_of_64: list of teams in the round of 64
    round_of_32: list of teams in the round of 32
    sweet16:     list of teams in the sweet 16
    elite8:      list of teams in the elite 8
    final4:      list of teams in the final 4
    championship:list of teams in the championship
    champion:    winner

This function will create a file with a filled out bracket
"""
def main(region_names, round_of_64, round_of_32, sweet16, elite8, final4, championship, champion):
    try:
        if ( len(round_of_64)  != 64 or
             len(round_of_32)  != 32 or
             len(sweet16)      != 16 or
             len(elite8)       != 8  or
             len(final4)       != 4  or
             len(championship) != 2  or
             len(champion)     <  1):
            print ("Error: Cannot Print Bracket! Incorrect Number of Teams")
            raise

        #Make a copy of final4
        final_four = collections.deque([])
        final_four.extend(final4)
        #Open an output file
        #f = open("bracket.txt", w+)
        #Print the Regions
        for i in range(0, len(region_names)):
            print("                                  " + str(region_names.pop()))
            print("1  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("16 " + str(round_of_64.pop()))
            print("                        " + str(sweet16.pop()))
            print("8  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("9  " + str(round_of_64.pop()))
            print("                                    " + str(elite8.pop()))
            print("5  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("12 " + str(round_of_64.pop()))
            print("                        " + str(sweet16.pop()))
            print("4  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("13 " + str(round_of_64.pop()))
            print("                                                " + str(final4.pop()))
            print("6  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("11 " + str(round_of_64.pop()))
            print("                        " + str(sweet16.pop()))
            print("3  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("14 " + str(round_of_64.pop()))
            print("                                    " + str(elite8.pop()))
            print("7  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("10 " + str(round_of_64.pop()))
            print("                        " + str(sweet16.pop()))
            print("2  " + str(round_of_64.pop()))
            print("            " + str(round_of_32.pop()))
            print("15 " + str(round_of_64.pop()))
            print("")
            print("")
            print("")
        print("                                  Final Four")
        print(" " + str(final_four.pop()))
        print("            " + str(championship.pop()))
        print(" " + str(final_four.pop()))
        print("                        " + champion + " is your champion!")
        print(" " + str(final_four.pop()))
        print("            " + str(championship.pop()))
        print(" " + str(final_four.pop()))
        print("")
        print("")


        #f.close()
        
    except:
        print ("Error: Exception Occurred in PrintBracket.py!")

