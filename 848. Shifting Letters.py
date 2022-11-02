class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        for i in range(len(s)):
            for ind in range(i+1):
                new_ascii = ord(s[ind])+shifts[i]%26
                while new_ascii>ord("z"):
                    new_ascii = ord("a") + new_ascii - ord("z") - 1
                s[ind] = chr(new_ascii)
        return "".join(s)
        
  # TLE
