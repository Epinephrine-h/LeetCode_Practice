class Solution(object):
    def compress(self, chars):
        i = 0
        write = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            cnt = j - i
            chars[write] = chars[i]
            write += 1
            if cnt > 1:
                for x in str(cnt):
                    chars[write] = x
                    write += 1
            i = j
        return write



        