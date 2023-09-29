from collections import deque
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("000")

        count = 1
        tmp = chars[0]
        chars.pop(0)

        if chars[0] == "000":
            chars.append(tmp)
            return len(chars.pop(0))

        while chars[0] != "000":
            if tmp == chars[0]:
                count += 1
            else:
                chars.append(tmp)
                if count != 1:
                    chars.extend(list(str(count)))
                count = 1
                tmp = chars[0]
            chars.pop(0)

        chars.append(tmp)
        if count != 1:
            chars.extend(list(str(count)))
        chars.pop(0)
        print(list(chars))
        return len(list(chars))
        