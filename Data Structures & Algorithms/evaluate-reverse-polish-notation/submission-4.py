def op(op, b, a):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return int(a / b)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = None
        for tok in tokens:
            print (tok, stack)
            if tok.isdigit() or len(tok) > 1 and tok[1:].isdigit():
                stack.append(int(tok))
            else:
                stack.append(op(tok, stack.pop(), stack.pop()))
        
        print (stack)
        return stack[0]