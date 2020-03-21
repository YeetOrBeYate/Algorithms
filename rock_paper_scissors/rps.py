#!/usr/bin/python

import sys



def rock_paper_scissors(n):

  result_array = []
  rotation = ['rock', 'paper', 'scissors']

  def recursive_listing(n, result=[]):

    if n == 0:
      return result_array.append(result)
      
    for x in rotation:
      recursive_listing(n -1, result + [x])

  recursive_listing(n)
  return result_array



print(rock_paper_scissors(2))





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')