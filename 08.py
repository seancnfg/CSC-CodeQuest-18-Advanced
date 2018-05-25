inp = open('Prob08.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    a, b, c = map(float, inp.readline().split())
    arr = [a, b, c]
    ans = []

    for x in arr:
        if x >= 180:
            y = round(x-180.0, 2)
            use = ""
            if y < 100:
                use += '0'
            if y < 10:
                use += '0'
            use += str(y)
            if len(use)== 3:
                use += '.'
            while len(use)< 6:
                use += '0'
            ans.append(use)
        else:
            y = round(x+180.0, 2)
            use = ""
            if y < 100:
                use += '0'
            if y < 10:
                use += '0'
            use += str(y)
            if len(use)== 3:
                use += '.'
            while len(use)< 6:
                use += '0'
            ans.append(use)
    print(" ".join(ans))
