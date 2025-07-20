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

#My Solution:
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

class solution:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def result(self):
        n1 = int(''.join(map(str, self.l1)))        #'map' turns l1 in a list of strings, 'join' joins them and 'int' does the rest
        n1 = int(str(n1)[::-1])                     #Reversing number

        n2 = int(''.join(map(str, self.l2)))
        n2 = int(str(n2)[::-1])

        r1 = n1 + n2                                #First result (sum of n1 and n2)
        r1 = int(str(r1)[::-1])                     #Reversing number

        r2 = [int(digit) for digit in str(r1)]      #Second result (r1 reversed changed into digits in a list
        return r2


print(solution(l1, l2).result())

#My Solution did not work on LeetCode because the platform passes linked lists (which I didn't even know),
#not arrays (Python List).

#A solution that meets the requirements by LeetCode to pass the test:
class Solution:

    def addTwoNumbers(self, l1, l2):
        def extract_number(node):
            num = ''
            while node:
                num += str(node.val)
                node = node.next
            return int(num[::-1])  # reverse the string and convert to int

        n1 = extract_number(l1)
        n2 = extract_number(l2)
        total = n1 + n2
        reversed_digits = str(total)[::-1]

        dummy = ListNode(0)
        current = dummy
        for digit in reversed_digits:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
