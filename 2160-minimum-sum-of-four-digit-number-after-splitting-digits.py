class Solution:
    def minimumSum(self, num: int) -> int:
        dig = list(map(int, str(num)))
        dig.sort()

        num1 = dig[0] * 10 + dig[2]
        num2 = dig[1] * 10 + dig[3]

        return num1+num2
