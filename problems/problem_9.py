# UNFINISHED

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2. For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# https://projecteuler.net/problem=9

# pyth_triplet = (a<b<c)
# c ** 2 = a ** 2 + b ** 2

# s = 1000
# a < s/3
# a < b < s/2

def calc_pyth_triplet(a, b, c, s):
  if a < b < c and a < s/3 and a < b < s/2:
    if a + b + c == 1000:
      goal = a + b + c
      print(goal)
    pass
  else:
    print("Invalid numbers. It is not a pythagorean triplet.")