class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                v2, v1 = stack.pop(), stack.pop()
                if token == '+':
                    res = v1 + v2
                if token == '-':
                    res = v1 - v2
                if token == '*':
                    res = v1 * v2
                if token == '/':
                    res = int(v1 / v2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0] 