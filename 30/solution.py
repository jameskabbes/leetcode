
class Solution:

    def isValidSubstring(self, s: str, n_char: int, n_words: int, word_counts: dict[str, int], remaining_words: set[str]) -> bool:

        for i in range(n_words):
            word = s[i*n_char: (i+1)*n_char]

            if word in remaining_words:
                word_counts[word] -= 1
                if word_counts[word] == 0:
                    remaining_words.remove(word)
                    if len(remaining_words) == 0:
                        return True

            else:
                return False

    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        n_char = len(words[0])
        n_words = len(words)

        set_words = set(words)
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

        valid_starting_inds = []
        for i in range(len(s) - (n_char*n_words)+1):

            string_to_check = s[i: i+(n_words*n_char)]
            if self.isValidSubstring(string_to_check, n_char, n_words, word_counts.copy(), set_words.copy()):
                valid_starting_inds.append(i)

        return valid_starting_inds


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(Solution().findSubstring(
    "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(Solution().findSubstring(
    "barfoofoobarthefoobarman", ["foo", "bar", "the"]))
print(Solution().findSubstring(
    "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
print(Solution().findSubstring(
    "lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))
