class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         w = s.split()  
         last_word = w[-1] 
         return len(last_word) 