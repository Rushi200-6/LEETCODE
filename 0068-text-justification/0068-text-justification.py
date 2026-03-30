class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Step 1: Find how many words fit in one line
            line_len = len(words[i])
            j = i + 1
            
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # Number of words in current line
            num_words = j - i
            line = ""
            
            # Step 2: If last line OR only one word → left justify
            if j == n or num_words == 1:
                for k in range(i, j):
                    line += words[k] + " "
                line = line.rstrip()  # remove extra space
                line += " " * (maxWidth - len(line))
            
            else:
                # Step 3: Distribute spaces evenly
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                spaces_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces_between + (1 if k - i < extra_spaces else 0))
                
                line += words[j - 1]  # last word (no extra space after)
            
            res.append(line)
            i = j
        
        return res