/**
 * @param {string} s
 * @return {string}
 */

var longestPalindrome = function(s) {

    // start from the longest substring, go to the smallest. return as soon as you find a palindrome
    // 0123456789

    /*
    Loop 1: substringLen = 10
    [ 0: len(s)-1 ] - 0123456789

    Loop 2: substringLen = 9
    [ 0: len(s)-2 ] - 012345678
    [ 1: len(s)-1 ] - 123456789

    Loop 3: substringLen = 8
    [ 0: len(s)-3 ] - 01234567
    [ 1: len(s)-2 ] - 12345678
    [ 2: len(s)-1 ] - 23456789
    */

    for ( var substringLen=s.length ; substringLen>0 ; substringLen-- ){

        for ( var i=0; i<s.length-substringLen+1 ; i++ ){
            var substring = s.substring(i, i+substringLen)
            if ( substring == substring.split('').reverse().join('') ){
                return substring
            }
        }
    }

};

let s = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"

console.log(longestPalindrome(s))