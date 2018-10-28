class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        hh, mm = time.split(':')
        digits = set(hh) | set(mm)
        digits = sorted(list(digits))
        n = len(digits)

        # new_mm > mm, return hh:new_mm
        for i in range(n):
            m0 = digits[i]
            if m0 < mm[0]: continue
            if m0 >= '6': break
            for j in range(n):
                m1 = digits[j]
                if int(m0 + m1) > int(mm):
                    return hh + ':' + m0 + m1

        min_mm = digits[0] + digits[0]

        # new_hh > hh, return new_hh:min_mm
        for i in range(n):
            h0 = digits[i]
            if h0 < hh[0]: continue
            if h0 > '3': break
            for j in range(n):
                h1 = digits[j]
                new_hh = int(h0 + h1)
                if new_hh < 24 and new_hh > int(hh):
                    return h0 + h1 + ':' + min_mm

        # next day, return min_hh:min_mm
        return min_mm + ':' + min_mm

sol = Solution()
time = '20:48'
print(sol.nextClosestTime(time))