class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagram_dict = {}  
    
        for s in strs:
            key = ''.join(sorted(s)) 
            
            if key in anagram_dict:
                anagram_dict[key].append(s)  
            else:
                anagram_dict[key] = [s]  
        result = list(anagram_dict.values())  
        return result