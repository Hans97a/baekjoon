T=int(input())

for i in range(T):
    score=0
    check=0
    Q=input()
    for q in range(len(Q)):
        if Q[q]=='X':
            check=0
        else:
            check+=1
            score+=check
    print(score)