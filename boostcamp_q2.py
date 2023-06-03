result = []


def reset_string(string, i):
    global result
    string += "." * i
    if len(string) == 8:
        result.append(string)
        string = ""
    return string


def solution(arr):
    global result
    string = ""
    i = 0
    for idx, memory_type in enumerate(arr):
        if len(string) == 8:
            result.append(string)
            string = ""

        if memory_type == "BOOL":
            string += "#"

        elif memory_type == "SHORT":
            if len(string) == 0:
                string += "##"
            else:
                i = len(string) % 2
                string = reset_string(string, i) + "##"
        elif memory_type == "FLOAT":
            if len(string) == 0:
                string += "####"
            else:
                i = len(string) % 4
                string = reset_string(string, i) + "####"

        elif memory_type == "INT":
            if len(string) == 0:
                result.append("########")
            else:
                i = 8 - len(string)
                string = reset_string(string, i)
                result.append("########")
        elif memory_type == "LONG":
            if len(string) == 0:
                result.append("########")
                result.append("########")
            else:
                i = 8 - len(string)
                string = reset_string(string, i)
                result.append("########")
                result.append("########")
    if len(string) != 0:
        string += "." * (8 - len(string))
        result.append(string)


arr = ["INT", "INT", "BOOL", "SHORT", "LONG"]
solution(arr)
answer = "".join(result)

if len(answer) > 128:
    print("HALT")
else:
    print(",".join(result))
