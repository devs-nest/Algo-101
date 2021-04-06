class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        parentHash = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) < 1:
                    return False

                if not s[i] == parentHash[stack.pop(-1)]:
                    return False

        return len(stack) == 0
