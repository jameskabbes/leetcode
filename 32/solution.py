


class Solution:

    def find_right_mate( self, s: str ):
        
        """
        given '(())' return, the index of the ')' character that matches the first '('
        """

        counter = 0
        for i in range( len(s) ):
            if s[i] == '(':
                counter -= 1
            elif s[i] == ')':
                counter += 1
            
            if counter == 0:
                return i
        
        return None
       

    def longestValidParentheses(self, s: str) -> int:

        while s[0] != '(':
            if len(s) == 1:
                return 0
            s = s[1:]
        while s[-1] != ')':
            if len(s) == 1:
                return 0
            s = s[:-1]

        matches = [ None,  ] * len(s)

        for i in range( len(s) ):
            
            if matches[i] == None:
                match_ind = self.find_right_mate( s[i:] )
                matches[ i ] = match_ind

                if match_ind != None:
                    matches[ i ] += i
                    matches[ matches[ i ] ] = i

        high_score = 0
        current_score = 0
        for i in range(len(matches)):
            
            #reset
            if matches[ i ] == None:
                if current_score > high_score:
                    high_score = current_score
                current_score = 0
            
            else:
                current_score += 1
            
        return max( current_score, high_score )

