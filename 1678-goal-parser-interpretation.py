class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        c = command.replace("()", "o")
        c = c.replace("(", "")
        c = c.replace(")", "")
        return c
