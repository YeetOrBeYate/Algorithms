#!/usr/bin/python

import argparse

# yeet = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]

def find_max_profit(prices):

  max_profit = float("-inf")

  for x in range(0,len(prices)):

    buy_value = x
    for y in range(buy_value+1,len(prices)):

      profit_value = prices[y] - prices[buy_value] 

      if profit_value >= max_profit:
        max_profit = profit_value
  
  return max_profit


# print(find_max_profit(yeet))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))