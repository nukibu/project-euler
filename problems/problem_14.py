# Finished
# Run in 43.14381814002991 seconds

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# https://projecteuler.net/problem=14

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

import sys
from time import time

def collatzSequence(min_val, max_val):

  term_list = []
  most_terms = 0

  for num in range(min_val, max_val):
    term_list.append(num)
    starting_num = num
    while num != 1:
      if num % 2 == 0:
        num = int(num/2)
        term_list.append(num) 
      else:
        num = int((num * 3) + 1)
        term_list.append(num)

    # Chaos
    if len(term_list) > most_terms:
      most_terms = len(term_list)
      highscore_terms = term_list
      highscore_num = starting_num
      term_list = []

    else:
      term_list = []

  print("Starting Number: " + str(highscore_num))
  print("The terms are: " + str(highscore_terms))
  print("Amount of terms: " + str(most_terms))

start = time()
collatzSequence(2, 1000000)
print(f'Time taken to run: {time() - start} seconds') 