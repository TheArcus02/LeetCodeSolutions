from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [word]
            else:
                dictionary[sorted_word].append(word)
        return list(dictionary.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

main()    