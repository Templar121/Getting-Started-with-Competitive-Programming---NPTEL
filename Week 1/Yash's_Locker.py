# Problem Statement

# Yash's Secure Locker: The Digital Root Password

# Yash owns a special locker to securely store his important letters. This locker has an advanced password mechanism. The password is determined based on the number of letters stored inside the locker. If there are letters, the password is the digital root of n
# .

# Your task is to write a program that calculates the password for the locker given the number of letters n
# .

# Digital Root:

# The digital root (also known as the repeated digital sum) of a number is the single-digit value obtained by iteratively summing the digits of the number until a single-digit result is achieved.

# For example:
# The digital root of 123 is calculated as follows: 1+2+3=6
# . The result is 6, a single digit, so the digital root is 6.

# Read more about digital root here

# Input Format

# The first line of the input contains a single integer t , representing the number of test cases.
# For each test case a single line is input containing a single positive integer representing the number of letters in the locker.

# Constraints

# 1≤t≤105
# n
#  is a positive integer.
# n
#  can be very large, up to 105
# .
# Output Format
# A single integer, the digital root of n



###############################################################################################################################
def digital_root(n):
    # Calculate the digital root using modulo 9 properties
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

# Read the number of test cases
t = int(input())
results = []

# Process each test case
for _ in range(t):
    n = input().strip()  # Read the large number as a string
    num = int(n) % 9  # Compute n % 9 directly from the string
    results.append(num if num != 0 else 9)  # Handle digital root directly

# Output results
print("\n".join(map(str, results)))