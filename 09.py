inp = open('Prob09.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    x, y = map(int, inp.readline().split(','))
    a = max(x, y)
    b = min(x, y)

    diff = abs(a-b)
    print(str(a) + "-" + str(b) + "=" + str(diff))
    while diff > 0:

        a = max(b, diff)
        b = min(diff, b)
        diff = abs(a-b)
        print(str(a) + "-" + str(b) + "=" + str(diff))
    if a == 1:
        print("COPRIME")
    else:
        print("NOT COPRIME")
