def basic_matching(s):
    c = 0
    for b in s:
        if b == "(":
            c += 1
        if b == ")":
            c -= 1

        if c < 0:
            return False

    return c == 0

def matching(s):
    stack = []
    for b in s:
        if b in "({[":
            stack.append(b)
        if b in "]})":
            if len(stack) == 0: return False;
            p = stack.pop()
            if b == ")" and p != "(": return False
            if b == "}" and p != "{": return False
            if b == "]" and p != "[": return False

    return len(stack) == 0

#print(basic_matching("()"))
#print(basic_matching("()(())"))
#print(basic_matching(")("))

#print(matching("()"))
#print(matching("{}"))
#print(matching("[]"))
#print(matching("]["))
#print(matching("((([{}]())){[[[]]]})"))

print(matching(")("))
print(matching("("))
print(matching("(]"))
