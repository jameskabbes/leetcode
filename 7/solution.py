class Solution:
    def reverse(self, x: int) -> int:
        
        positive = True
        if x < 0:
            positive = False

        x = str(x)
        if not positive:
            x = x[1:]            
        
        reversed = int(x[::-1])
        if reversed > (2**31):
            return 0
        
        if not positive:
            reversed *= -1
        return reversed
        

print (Solution().reverse( 120 ))