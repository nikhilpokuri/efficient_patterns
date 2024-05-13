class Solution:
    def __init__(self):
        self.currLen = 0
        self.res = ''
    def longest_Palindromic_Substring(self, s):
        if len(s) == 1:
            return s
        def around_center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) + 1 > self.currLen:
                    self.res = s[l:r+1]
                    self.currLen = (r-l) + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            '''
            for every ith character 
            we will check before and after characters of i till they aren't equal
            '''
            around_center(i,i) #odd eg:- bab
            around_center(i,i+1) #even eg:- baab
        return self.res
obj = Solution()
s = input("Enter String: ")
print(obj.longest_Palindromic_Substring(s))