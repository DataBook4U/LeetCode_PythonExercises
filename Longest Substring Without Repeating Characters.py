"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class solution:

    def __init__(self, input):
        self.input = input

    #I think of iterating through the string and adding substrings to a list. Then the substring in the list with the highest len() value gets returned
    #Update: it might be better using a set instead of a list
    def lengthOfLongestSubstring(self):
        substrings = []
        sequences = []
        i = 0
        j = 1
        length = len(self.input)

        #Place string in array
        while i < length:
            substrings.append(self.input[i])
            i += 1

        #Determine sequences in array
        for i in range(0, length):
            substrings = "".join(substrings)
            sequences.append(substrings)


        return sequences


s = "abcabcbb"
trial1 = solution(s)
print(trial1.lengthOfLongestSubstring())