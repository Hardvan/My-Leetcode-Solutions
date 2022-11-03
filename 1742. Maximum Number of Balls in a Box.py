class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for ball_no in range(lowLimit, highLimit+1):
            digits_sum = sum(map(int, str(ball_no)))
            if digits_sum in boxes:
                boxes[digits_sum] += 1
            else:
                boxes[digits_sum] = 1
        return max(boxes.values())
