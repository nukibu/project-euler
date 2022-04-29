# Unfinished

# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# https://projecteuler.net/problem=21

amicable_num = []

def d(number):

  div_list = []

  for i in range(1, number):
    if number % i == 0:
      div_list.append(i)

    div_sum = sum(div_list)
    print("d(" + str(i+1) + ") = " + str(div_sum))
    if d(i+1) == d(div_sum):
      amicable_num.append(i+1)
      amicable_num.append(div_sum)


d(220)


