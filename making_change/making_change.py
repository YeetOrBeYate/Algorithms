#!/usr/bin/python

import sys

waysD = [1,5,10,25,50]
amount = 10

def making_change(amount, denominations):

  ways = [1] + [0] * (amount)
  print(ways)

  for coin in denominations:
    for place in range(coin, amount + 1):
      ways[place] = ways[place] + ways[place - coin]
  return ways[amount]

print(making_change(amount, waysD))

# if __name__ == "__main__":
#   # ways our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")