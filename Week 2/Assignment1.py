# You are the sports teacher of a school. There are n
#  students in your class. You ask the students to stand in a line according to their heights. They then run laps on a circular ground while still maintaining the same order. After an arbitrary number of laps, you ask the students to stand in a line again. However, now some students might have done one more lap than the others and thus have moved ahead of the others. Their circular order is still maintained.

# However, as the ground is pretty big, you suspect a particular student might be missing. You are given the heights of the students in the current order, and the height of the target student. Find if the target student is present in the queue.

# Input Format

# The first line of input contains a single integer t
# , denoting the number of test cases.
# Each test case consists of two lines.
# The first line of each test case contains two integers n
#  and x
# , denoting the number of students and the height of the target student.
# The second line of each test case contains n
#  integers a1,a2,....,an
# , denoting the heights of the students in the current order.




#############################################################################################################################



def find_student(t, test_cases):
    results = []
    for case in test_cases:
        n, x, a = case
        # Perform a linear search to find x in the array a
        index = -1
        for i in range(n):
            if a[i] == x:
                index = i
                break
        results.append(index)
    return results

# Input reading
t = int(input())  # Number of test cases
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, x, a))

# Process each test case and print results
results = find_student(t, test_cases)
for res in results:
    print(res)