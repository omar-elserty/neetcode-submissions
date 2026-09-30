class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        last = len(s) - 1
        first = 0
        while last>first :
            if  not s[first].isalnum():
                first += 1
                continue

            if  not s[last].isalnum():
                last-=1
                continue

            s=s.lower()

            if s[first]!=s[last]:
                return False
            first+=1
            last-=1
        return True
        