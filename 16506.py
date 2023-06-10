N = int(input())

for i in range(N):
    oper, fisrt, second, third = input().split()
    result = ""

    if "ADD" in oper:
        result += "00001" if "C" in oper else "00000"
    elif "SUB" in oper:
        result += "00011" if "C" in oper else "00010"
    elif "MOV" in oper:
        result += "00101" if "C" in oper else "00100"
    elif "AND" in oper:
        result += "00111" if "C" in oper else "00110"
    elif "OR" in oper:
        result += "01001" if "C" in oper else "01000"
    elif "NOT" == oper:
        result += "01010"
    elif "MULT" in oper:
        result += "01101" if "C" in oper else "01100"
    elif "LSFTL" in oper:
        result += "01111" if "C" in oper else "01110"
    elif "LSFTR" in oper:
        result += "10001" if "C" in oper else "10000"
    elif "ASFTR" in oper:
        result += "10011" if "C" in oper else "10010"
    elif "RL" in oper:
        result += "10101" if "C" in oper else "10100"
    else:
        result += "10111" if "C" in oper else "10110"

    result += "0"
    binary = bin(int(fisrt))[2:]
    result += "0" * (3 - len(binary)) + binary
    binary = bin(int(second))[2:]
    result += (
        "0" * (3 - len(binary)) + binary
        if oper != "NOT" and "MOV" not in oper
        else "000"
    )

    if result[4] == "1":
        binary = bin(int(third))[2:]
        result += "0" * (4 - len(binary)) + binary
    else:
        binary = bin(int(third))[2:]
        result += "0" * (3 - len(binary)) + binary + "0"
    print(result)
