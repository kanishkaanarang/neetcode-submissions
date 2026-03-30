from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Create an empty dictionary
        anagram_map = {}

        # Step 2: Loop through each string in the input list
        for word in strs:
            
            # Step 3: Sort the word
            sorted_word = sorted(word)
            
            # Step 4: Convert sorted list into a string (so it can be used as a key)
            key = ''.join(sorted_word)
            
            # Step 5: Check if key already exists in dictionary
            if key in anagram_map:
                # If yes, append the word to the existing list
                anagram_map[key].append(word)
            else:
                # If no, create a new list with this word
                anagram_map[key] = [word]

        # Step 6: Extract all grouped values
        result = []
        for key in anagram_map:
            result.append(anagram_map[key])

        # Step 7: Return the result
        return result