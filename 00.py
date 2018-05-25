inp = open('Prob00.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    n = int(inp.readline())

    for x in range(n):
        s = inp.readline().strip()

        print(s)
        
