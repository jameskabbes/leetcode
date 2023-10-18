from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s = ''
        strs = sorted( strs )

        for position in range( min(len(strs[0]), len(strs[-1]) ) ):
            
            if strs[0][position] != strs[-1][position]:
                return s

            s += strs[0][position]
        return s                
  
    
#print (Solution().longestCommonPrefix( ["flower","flow","flight"] ))
print (Solution().longestCommonPrefix( ["a"] ))