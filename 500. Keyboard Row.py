class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        diction = {"qwertyuiop": 1, "asdfghjkl": 2, "zxcvbnm": 3}
        ans = []
        for word in words:
            first_ch = word[0].lower()
            cur_row = 0
            for row in diction:
                if first_ch in row:
                    cur_row = diction[row]
                    break
            for ch in word:
                next_row = 0
                for row in diction:
                    if ch.lower() in row:
                        next_row = diction[row] 
                        break
                if next_row!=cur_row:
                    break
            else:
                ans.append(word)
        
        return ans
