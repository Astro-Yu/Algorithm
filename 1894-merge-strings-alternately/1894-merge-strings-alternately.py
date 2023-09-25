class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_word_list = []
        for i in range(len(word1)):
            new_word_list.insert(i*2,word1[i])
        for j in range(len(word2)):
            new_word_list.insert(j*2+1,word2[j])
        new_word = ''.join(new_word_list)
        return new_word