class Solution:
    def isPalindrome(self, x: int) -> bool:

        string = str(x)
        for i in range( len(string)//2 + 1 ):
            if string[i] != string[ -1*( i+1 ) ]:
                return False
        return True
       

print (Solution().isPalindrome( 121 ))
print (Solution().isPalindrome( -121 ))
print (Solution().isPalindrome( 10 ))
print (Solution().isPalindrome( 101101 ))

        