
n = 7 

a = [[ 1 if i % 2 == 0 else 0 for i in range(n)] for j in range(n)]

for r in a:
        print(*r)