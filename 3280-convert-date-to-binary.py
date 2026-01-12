class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y, m, d = date.split("-")
        return "{}-{}-{}".format(
            bin(int(y))[2:], 
            bin(int(m))[2:], 
            bin(int(d))[2:]
        )
