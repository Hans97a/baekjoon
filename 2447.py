N=int(input())
arr=[[' ' for i in range(N)] for j in range(N)]

def recursive(n):
    div=n//3
    if n==3:
        arr[0][:3]=['*']*3
        arr[2][:3]=['*']*3
        arr[1]=['*', ' ', '*']
        return

    recursive(div)
    
    for i in range(0, n, div):
        for j in range(0, n, div):
            if i != div or j != div:
                for k in range(div):
                    arr[i+k][j:j+div]= arr[k][:div]
                    
recursive(N)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end="")
    print()