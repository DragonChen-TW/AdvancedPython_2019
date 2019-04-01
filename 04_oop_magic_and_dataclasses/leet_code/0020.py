class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        c_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if stack:
                    if stack[-1] != c_dict[c]: # if [)
                        return False
                    else:
                        stack.pop()
                else: # if [])
                    return False

        if not stack:
            return True
        else: # if ([]
            return False

if __name__ == '__main__':
    s = Solution()
    inputs = ["()", "()[]{}", "(]", "([)]", "{[]}"]

    for i in inputs:
        print(s.isValid(i))
