class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        dict1={}
        #i is the word
        for i in strs:
            word = list(i)
            word.sort()
            word = "".join(word)
            if word not in dict1:
                dict1[word]=[i]
            else:
                dict1[word].append(i)
        
        for value in dict1.values():
            res.append(value)
        return res
            
        