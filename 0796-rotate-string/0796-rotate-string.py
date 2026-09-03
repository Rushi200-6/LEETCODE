class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        c_s=s+s
        if goal in c_s:
            return True
        return False