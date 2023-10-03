class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1 = list(word1)
        word2 = list(word2)
        word1_count = []
        word2_count = []

        if len(word1) != len(word2):
            return False
        elif sorted(list(set(word1))) == sorted(list(set(word2))):
            for i in list(set(word1)):
                count1 = 0
                count2 = 0
                count1 = word1.count(i)
                count2 = word2.count(i)

                word1_count.append(count1)
                word2_count.append(count2)

            if sorted(word1_count) == sorted(word2_count):
                return True
                
            return False 

        