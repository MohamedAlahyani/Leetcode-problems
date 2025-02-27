class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Quick check: Different lengths can't be anagrams
            return False

        stack = []  # Using a list as a stack

        for char in t:
            stack.append(char)  # Push characters of t into the stack

        reversed_t = ""  
        while stack:
            reversed_t += stack.pop()  # Pop characters to reverse t

        return sorted(s) == sorted(reversed_t)  # Compare sorted versions
