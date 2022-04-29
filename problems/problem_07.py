# Finished
# Run in 0.42087507247924805 seconds

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# https://projecteuler.net/problem=7

import sys
from time import time

prime_list = []

def isprime(num):
  for n in range(2, int(num**0.5)+1):
    if num%n==0:
      return False
  return True

# min_val = 1 excludes 1
# max_val should correspond to sys.maxsize**10 (potentially even higher)
# nth_prime_number = 5; gives out the 5th prime number

def checkPrimeNumbers(min_val, max_val, nth_prime_number):
  i = min_val
  for i in range(min_val, max_val):
    if isprime(i) == True:
      prime_list.append(i)
    i += 1
    if len(prime_list) == nth_prime_number + 1:
      print(prime_list[-1])
      break

start = time()
checkPrimeNumbers(1, sys.maxsize**10, 10001)
print(f'Time taken to run: {time() - start} seconds')