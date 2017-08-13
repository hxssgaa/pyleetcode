import random
import string


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        if not s or not t:
            return res
        """
        t_map is the character of t maps to its occurrences, while the window is the character of window
        maps to its occurrences in the range of (slow: fast)
        """
        t_map, window = [0 for _ in range(256)], [0 for _ in range(256)]
        slow, fast, letter_cnt, min_letter = 0, 0, 0, 1 << 30
        for c in t:
            t_map[ord(c)] += 1
        while fast < len(s):
            ch = s[fast]
            if t_map[ord(ch)] > 0:
                if window[ord(ch)] < t_map[ord(ch)]:
                    letter_cnt += 1
                window[ord(ch)] += 1
            if letter_cnt == len(t):
                while t_map[ord(s[slow])] == 0 or (window[ord(s[slow])] > t_map[ord(s[slow])]):
                    if window[ord(s[slow])] > t_map[ord(s[slow])]:
                        window[ord(s[slow])] -= 1
                    slow += 1
                if fast - slow + 1 < min_letter:
                    min_letter = fast - slow + 1
                    res = s[slow: slow + min_letter]
                window[ord(s[slow])] -= 1
                slow += 1
                letter_cnt -= 1
            fast += 1
        return res


str = "".join(random.choice(string.ascii_lowercase) for _ in range(10000))
print(Solution().minWindow(str, "qwekqwjekqwjdznxcmzxnmcnzxmcaskjkajdqpweioqwieoqwieosjkdfsdnvsdncmcdskmkfqwe"))
