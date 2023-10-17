
def is_palindrome( s: str ):
    return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = s[0]
   
        # loop from the start to end
        for i in range( len(s) ):
            print ('i: ', i)

            # A-B-A
            # one letter in center
            for j in range( len(longest)//2, min( i, len(s)-i-1 )+1 ):
                print ('j: ', j)
                
                substring = s[ i-j:i+j+1 ]
                print (substring)
                
                if is_palindrome(substring):
                    longest = substring               
                else:
                    # if B-C-D isn't a palindrome, then neither is A-B-C-D-A, abandon this for loop
                    break

            # A-B-B-A
            for j in range( len(longest)//2, min( i, len(s)-i-2 )+1 ):
                print ('j: ', j)
    
                substring = s[ i-j:i+j+2 ]
                print (substring)

                if is_palindrome(substring):
                    longest = substring               
                else:
                    break
            
        return longest

s = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
#s = 'abcdeababcdcba'
#s = 'ccc'
answer = Solution().longestPalindrome( s )
print ()
print (answer)

