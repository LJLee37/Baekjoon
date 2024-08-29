line = input()
while line != ".":
    bracketsStack = []
    isBalanced = True
    for char in line:
        if char == "(" or char == "[":
            bracketsStack.append(char)
        elif char == ")":
            if bracketsStack == []:
                print("no")
                isBalanced = False
                break
            if bracketsStack[-1] == "(":
                bracketsStack.pop()
            else:
                print("no")
                isBalanced = False
                break
        elif char == "]":
            if bracketsStack == []:
                print("no")
                isBalanced = False
                break
            if bracketsStack[-1] == "[":
                bracketsStack.pop()
            else:
                print("no")
                isBalanced = False
                break
    if isBalanced:
        if bracketsStack == []:
            print("yes")
        else:
            print("no")
    line = input()
