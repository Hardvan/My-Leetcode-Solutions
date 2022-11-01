class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        tiring = [int(i>8) for i in hours]
        n = len(tiring)
        maxi = 0
        for len_int in range(n,0,-1): # n to 1
            for start in range(0,n-len_int+1):
                a = tiring[start:start+len_int].count(1)
                if a>len_int-a and len_int>maxi:
                    maxi = len_int
        return maxi
      
 # TLE
