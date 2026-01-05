class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        num = 0
        for c in capacity:
            total -= c
            num += 1
            if total <= 0:
                break
        return num
