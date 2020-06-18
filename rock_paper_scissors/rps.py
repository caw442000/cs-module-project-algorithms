#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
    # n is the number of players

    # if n is 4 ['rock', 'rock', 'rock', 'paper']
    # need to make sure each location goes through each rock paper scissors
    # only 1 item can change at a time
    # for each list location location[0] ---> location[n] cycle through rock,paper,scissors

  pass

def rps_helper(number_players, element, location, count):
    element = element
    number_players = number_players
    location = location
    count = 3
    rps_list = [element] * number_players
    
    # base case if count is 0 return 
    if count == 0: 
        return 
    else:
        while count > 0:

            rps_list
            count -= 1




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')