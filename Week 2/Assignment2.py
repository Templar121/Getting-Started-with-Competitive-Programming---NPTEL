# During the pandemic era of 2020, Chennai faced a severe outbreak of COVID-19. A citywide lockdown was imposed, restricting people from leaving their homes. To ensure citizens had access to essential supplies like food and medicine, the State Government of Chennai devised a plan to use drones for contactless delivery, maintaining strict social distancing protocols.

# Each drone has a fixed carrying capacity, represented as an integer in the array capacities , and all drones are identical in functionality apart from their carrying capacity. To optimize the delivery process and minimize resource wastage, the government aims to select exactly x
#  drones such that each of these x
#  drones has a carrying capacity of at leastx
#  . This selection process ensures the fleet's efficiency aligns with the demand for heavier deliveries.

# Your task is to determine the "critical capacity" x
#  , such that exactly x
#  drones can meet this x
# criterion. If no such x
#  exists, return −1
#  . It is guaranteed that if a "critical capacity" exists, it will be unique

# Input Format

# The first line of the input contains a single integer t, representing the number of test cases.
# For each test case, the input consists of two lines:
# The first line contains a single integer n
# , the length of the array.
# The second line contains $n$ space-separated positive integers, representing the array capacities.

######################################################################################################################################

def find_critical_capacity(t, test_cases):
    results = []
    for case in test_cases:
        n, capacities = case
        capacities.sort(reverse=True)  # Sort in descending order
        
        critical_x = -1
        for x in range(1, n + 1):  # Check for each potential x
            if capacities[x - 1] >= x and (x == n or capacities[x] < x):
                critical_x = x
                break
        
        results.append(critical_x)
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])  # Number of test cases
test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    capacities = list(map(int, data[index + 1:index + 1 + n]))
    test_cases.append((n, capacities))
    index += 1 + n

# Process each test case and print results
results = find_critical_capacity(t, test_cases)
sys.stdout.write("\n".join(map(str, results)) + "\n")