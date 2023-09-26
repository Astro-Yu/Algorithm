class Solution(object):
    def compress(self, chars):
        new_word = []
        n = 1

        if len(chars) == 1:
            new_word = chars
        else:

            for i in range(1,len(chars)):
                if chars[i-1] == chars[i]:
                    n += 1
                    if i == len(chars)-1:
                        new_word.append(chars[i-1])
                        if n != 1:
                            new_word.append(str(n))
                elif chars[i-1] != chars[i]:
                    new_word.append(chars[i-1])
                    if n != 1:
                        new_word.append(str(n))
                    if i == len(chars)-1:
                        new_word.append(chars[i])
                    n = 1

        new_word  = "".join(new_word)    

        for i in range(len(new_word)):
            chars[i] = list(new_word)[i]
        return len(chars[:len(new_word)])