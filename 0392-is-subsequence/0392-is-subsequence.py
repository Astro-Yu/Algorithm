class Solution(object):
    def isSubsequence(self, s, t):
        
        s_str = list(s)
        t_str = list(t)
        n = 0
        slice = 0
        doublebreak = True

        for i in range(len(s_str)):
            for j in range(slice,len(t_str)):
                slice += 1
                if s_str[i] == t_str[j]:
                    n += 1
                    break

        if len(s_str) == n:
            return True
        else:
            return False
 