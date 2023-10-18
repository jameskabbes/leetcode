
places = [

    {
        1: 'I',
        5: 'V',
    },
    {
        1: 'X',
        5: 'L',
    },
    {
        1: 'C',
        5: 'D',
    },
    {
        1: 'M',
    }
]


class Solution:
    def intToRoman(self, num: int) -> str:

        s = ''
        num_str = str(num)

        print (num_str)

        for i in range(len(num_str)):

            place_s = ''
            digit = int(num_str[-(i+1)])

            print ('--------------')
            print (digit)

            if digit == 9:
                # IX
                place_s = places[ i ][ 1 ] + places[ i+1 ][ 1 ]

            else:

                if digit >= 5:
                    place_s = places[ i ][ 5 ]
                    digit -= 5

                if digit == 4:
                    # IV
                    place_s += places[ i ][ 1 ] + places[ i ][ 5 ] 

                else:
                    for _ in range(digit):
                        place_s += places[ i ][ 1 ]

            print (place_s)

            s = place_s + s

        return s


print (Solution().intToRoman(3999))