
roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

subtractors = {
    'I': {'V', 'X'},
    'X': {'L', 'C'},
    'C': {'D', 'M'},
}


class Solution:
    def romanToInt(self, s: str) -> int:
        
        total = 0
        i = 0
        while i < len(s):
            
            char = s[i]
            if char not in subtractors:
                total += roman_numerals[ char ]
            else:
                if i != len(s)-1 and s[i+1] in subtractors[char]:
                    total += roman_numerals[ s[i+1] ]
                    total -= roman_numerals[ char ]
                    i += 1
                    
                else:
                    total += roman_numerals[ char ]

            i += 1                

        return total






print (Solution().romanToInt('MCMXCIV'))