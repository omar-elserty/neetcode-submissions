class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict 1 is number in list ---> frequency
        #dict 2 is the reverse
        dict1 = {}
        dict2={}

        counter = 0

        
        
        


        for i in nums:
            if i in dict1:
                dict1[i] = dict1[i] + 1
                
            else:
                dict1[i] = 1
            
            


        for i,j in dict1.items():
            if j in dict2.keys():
                temp=dict2[j]
                temp.append(i)
                dict2[j]=temp

            else:
                dict2[j]=[i]

        dict2=dict(sorted(dict2.items(),reverse=True))


        all_ordered = [item for sublist in dict2.values() for item in sublist]
        counter = 0
        final_answer = []

        while counter<k:
            final_answer.append(all_ordered[counter])
            counter = counter + 1
        
        return final_answer
                








        
