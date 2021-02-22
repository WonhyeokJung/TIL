stack = []
test_case = input()
for i in test_case:
    if i == "(" or i == "{" or i == "[":
        stack.append(i)

    elif not len(stack):
        print("error")
        break

    elif i == ")":
        if stack[len(stack)-1] == "(":
            stack.pop(-1)
        else:
            print("error")
            break

    elif i == "}":
        if stack[len(stack)-1] == "{":
            stack.pop(-1)
        else:
            print("error")
            break

    elif i == "]":
        if stack[len(stack)-1] == "[":
            stack.pop(-1)
        else:
            print("error")
            break

if not stack:
    print("True")

