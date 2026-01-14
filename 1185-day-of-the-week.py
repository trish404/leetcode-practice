class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        lengs = [31,28,31,30,31,30,31,31,30,31,30,31]

        def leap(year):
            return year%400 == 0 or (year%4 == 0 and year%100 != 0 )
        
        tot = 0
        for y in range(1971, year):
            tot += 366 if leap(y) else 365
        
        for m in range(1, month):
            if m== 2 and leap(year):
                tot += 29
            else:
                tot += lengs[m-1]
        
        tot += day
        return days[(tot + 4) % 7]
