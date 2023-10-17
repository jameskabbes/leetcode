class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        valid = [ False, ] * len(s)
        valid = self.get_length( s, valid )
        
        longest = 0
        in_chain = False
        print (valid)
        for i in range( len(valid) ):
            
            if valid[i]:
                if in_chain:
                    current += 1                
                else:
                    in_chain = True
                    current = 1
            else:
                if in_chain:
                    in_chain = False
                    if current > longest:
                        longest = current

        if current > longest:
            longest = current
        
        return longest        
        
    def get_length( self, s: str, valid ):

        print ('Calling get length')
        print (valid)

        left = 0
        changed = False
        while left < len(s) -1:

            print ('Left: ', left)

            if valid[left]:
                left += 1
                continue

            if s[left] == '(':

                right = left+1
                while right < len(s):

                    print ('Right: ', right)

                    if not valid[right]:
                        if s[right] == ')':
                            print ('------Valid!--------')
                            changed = True
                            valid[left] = True
                            valid[right] = True
                            left = right
                        break                    
                    
                    # if these are valid parentheses, keep going                    
                    if valid[right]:
                        right += 1

            left += 1

        if changed:
            return self.get_length( s, valid )
        else:
            return valid

