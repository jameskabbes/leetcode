
def get_n_repeats( numRows: int ) -> int:
    
    if numRows == 1:
        return 1
    else:
        return (numRows-1)*2


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        new_s = ''
        repeats = get_n_repeats(numRows)
        
        # top row: 0
        print ('top row')
        for i in range( 0 , len(s), repeats):
            new_s += s[i]
        print (new_s)

        print ('middle rows')

        # middle rows: 1,7; 2,6; 3,5
        for i in range( 0, (repeats-2)//2 ):
            
            left_offset = i+1
            right_offset = repeats-left_offset
            
            print (left_offset, right_offset)
            for j in range( 0, len(s), repeats):
                
                if len(s) > (j+left_offset):
                    new_s += s[ j + left_offset  ]
                if len(s) > (j+right_offset):
                    new_s += s[ j + right_offset ]

        # bottom row: 4
        print ('bottom row')
        
        if repeats > 1:
            for i in range( repeats//2 , len(s), repeats):
                new_s += s[i]

        print (new_s)
        return new_s
        
#print (Solution().convert( 'PAYPALISHIRING', 4 ) )
print (Solution().convert( 'ABCD', 3 ) )
