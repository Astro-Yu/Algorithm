class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        net_alt = 0
        for i in range(len(gain)):
            net_alt += gain[i]

            if net_alt > result:
                result = net_alt

        return result 

