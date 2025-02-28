# Problem Statement

# Rahul is looking for some special numbers. The numbers he is looking for should satisfy a specific constraint. The number, when prime factorized, should contain all prime factors of the same parity.
# Further, the number itself should be an even number.
# Help Rahul in identifying if a number is special or not.

# Prime Factorization:

# Prime factorization is the process of finding the prime numbers that multiply together to make a number. A prime number is a number that is greater than 1 and divided by 1 and itself only. The prime factorization of a number is the product of prime numbers that multiply together to make the original number. Every number has a unique prime factorization.

# Parity:

# Parity is a mathematical term that describes the property of an integer's inclusion in one of two categories: even or odd. An integer is even if it is 'evenly divisible' by 2, meaning it yields no remainder when divided by 2. An integer is odd if it is not even.

# Input Format

# The first line of input contains a single integer t, which is the number of test cases.
#  t test cases follow.
# Each test case consists of a single line containing a single integer n, which is the number to check.

# Constraints

# 		1≤t≤105

#  	       	1≤n≤260


# Output Format

# For each test case, print "YES" if the number is special, else print "NO".


#################################################################################

def is_special(n):
    # Check if n is even and a power of 2
    return n > 0 and n % 2 == 0 and (n & (n - 1)) == 0

# Read number of test cases
t = int(input())
results = []

# Process each test case
for _ in range(t):
    n = int(input())
    if is_special(n):
        results.append("YES")
    else:
        results.append("NO")

# Output results
print("\n".join(results))