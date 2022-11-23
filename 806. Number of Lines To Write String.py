class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width_used = 0
        for ch in s:
            w = widths[ord(ch)-ord("a")]
            if width_used + w <= 100: # Current Line
                width_used += w
                continue
            else: # Next Line
                width_used = w
                lines += 1
        return [lines,width_used]
