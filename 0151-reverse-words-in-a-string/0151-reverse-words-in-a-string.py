class Solution(object):
    def reverseWords(self, s):
        new_word = []
        str_list = s.split(" ")
        str_list = list(filter(None, str_list))

        for i in range(len(str_list)):
            new_word.append(str_list[-1-i])

        return " ".join(new_word)