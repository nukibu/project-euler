# Finished
# Run in 20.966672658920288 seconds

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# https://projecteuler.net/problem=10

import sys
from time import time

prime_list = []
min_val = 2
max_val = 2000000

def isprime(num):
  for n in range(2, int(num**0.5)+1):
    if num%n==0:
      return False
  return True

# min_val = 1 excludes 1
# max_val should correspond to sys.maxsize**10 (potentially even higher)
# nth_prime_number = 5; gives out the 5th prime number

def checkPrimeNumbers(min_val, max_val):
  i = min_val
  for i in range(min_val, max_val):
    if isprime(i) == True:
      prime_list.append(i)
  print(sum(prime_list))
    
start = time()
checkPrimeNumbers(min_val, max_val)
print(f'Time taken to run: {time() - start} seconds')