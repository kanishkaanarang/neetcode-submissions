class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s)!=len(t):
            return False
        for char in s:
            if char not in dic:
                dic[char]=1
            else:
                dic[char]+=1
        
        for char in t:
            if char not in dic:
                return False
            else:
                dic[char]-=1
        
        for key,val in dic.items():
            if val!=0:
                return False
        return True        