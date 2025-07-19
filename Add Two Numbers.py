"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers
and return the sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

l1 = [2, 4, 3]
l2 = [5, 6, 4]

class solution:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def result(self):
        n1 = int(''.join(map(str, self.l1)))        #'map' turns l1 in a list of strings, 'join' joins them and 'int' does the rest
        n1 = int(str(n1)[::-1])
        n2 = int(''.join(map(str, self.l2)))

        print(n1)

solution(l1, l2).result()
