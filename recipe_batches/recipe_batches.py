#!/usr/bin/python

import math

yeet = { 'milk': 2, 'sugar': 40, 'butter': 20, "go":90 }

yate = { 'milk': 5, 'sugar': 120, 'butter': 500 }

def recipe_batches(recipe, ingredients):



  if len(recipe) != len(ingredients):
    return 0

  max_amount = float('inf')

  for x in recipe:
    divide = math.floor(ingredients[x]/recipe[x])
    if divide <= max_amount:
      max_amount = divide
  
  return max_amount


print(recipe_batches(yeet,yate))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))