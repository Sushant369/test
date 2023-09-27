class Solution:
   def isStrictlyPalindromic(self, n: int) -> bool:
        count = 0
        for i in range(2,n+1):
            bit = ''
            dup = n
            while dup!=0:
                print(dup)
                d = dup % i
                bit = str(d) + bit
                print(bit)
                dup = dup // i

            rev = bit[::-1]
                    
            if rev == bit:
                count += 1

        if count == n-2:
            return True



sol=Solution()
list =9
# print(list.sort())
sol.isStrictlyPalindromic(list)