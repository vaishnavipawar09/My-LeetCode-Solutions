class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)     #create a default dict hashmap

        for words in strs:              # for each word in the string
            count = [0] * 26            #cal the freq of each word

            for ch in words:            #for each character in the word
                count[ord(ch) - ord("a")] += 1      # cal the fre of each char in word
            
            hashmap[tuple(count)].append(words)     #add the freq and char in the hashmap
        
        return list(hashmap.values())   #return the group of anagrams

# Time: O(n * k), n = number of strings, k = max length of a string (≤ 100)
# Space: O(n * k)  Storing frequency keys + grouped strings

#Dry Run:["eat","tea","tan","ate","nat","bat"]
# "eat" → (1,0,0,0,1,0,...,1) → bucket A
# "tea" → same tuple → bucket A
# "ate" → same tuple → bucket A
# "tan" → different tuple → bucket B
# "nat" → same as "tan" → bucket B
# "bat" → unique tuple → bucket C
# Output : [["eat","tea","ate"], ["tan","nat"], ["bat"]]

#Pattern : Canonical Representation → Hashmap Grouping
# Use this when: 1. You need to group items
# 2. Order doesn’t matter
# 3. You can compute a unique “signature” for each group