inp = open('Prob01.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    n = int(inp.readline().strip())

    if n >= 70:
        print("PASS")
    else:
        print('FAIL')
