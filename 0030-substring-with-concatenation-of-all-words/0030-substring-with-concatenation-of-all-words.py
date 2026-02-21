from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        n = len(s)

        target_count = Counter(words)
        result = []

        
        for i in range(word_len):
            left = i
            curr_count = defaultdict(int)
            words_used = 0

           
            for right in range(i, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target_count:
                    curr_count[word] += 1
                    words_used += 1

                   
                    while curr_count[word] > target_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        words_used -= 1

                    
                    if words_used == total_words:
                        result.append(left)

                else:
                   
                    curr_count.clear()
                    words_used = 0
                    left = right + word_len

        return result