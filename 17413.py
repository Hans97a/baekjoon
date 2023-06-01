string = input()
tag_stack = []
string_stack = []

for idx, char in enumerate(string):
    if not tag_stack and char not in ("<", ">"):
        if char == " ":
            string_stack.reverse()
            print("".join(string_stack), end=" ")
            string_stack.clear()
        elif idx == len(string) - 1:
            string_stack.append(char)
            string_stack.reverse()
            print("".join(string_stack))
        else:
            string_stack.append(char)
    else:
        if string_stack:
            string_stack.reverse()
            print("".join(string_stack), end="")
            string_stack.clear()

        if char == ">":
            tag_stack.append(char)
            print("".join(tag_stack), end="")
            tag_stack.clear()
        else:
            tag_stack.append(char)
