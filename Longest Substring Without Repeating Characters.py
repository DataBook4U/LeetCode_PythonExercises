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
        seen = set()    #Here the chars are being stored of the string that is being looked at
        left = 0        #Left side of the string
        max_len = 0     #Saves max length of the valid substrings (duplicate free, thanks to the set)

        #Moving with a right pointer through the string:
        for right in range(len(self.input)):
            while self.input[right] in seen:                #If current char already in set, move left pointer right and dump char until duplicates are out
                seen.remove(self.input[left])
                left +=1

            #self.input[right] not in Set -> add to set
            seen.add(self.input[right])

            #update max_len if substring is longer
            max_len = max(max_len, right - left + 1)

        #give back max_len of the found substrings:
        return max_len


s = "dvdf"
trial1 = solution(s)
print(trial1.lengthOfLongestSubstring())