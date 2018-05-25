inp = open('Prob10.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    r, c = map(int, inp.readline().split(","))
    startX, startY = map(int, inp.readline().split(","))
    endX, endY = map(int, inp.readline().split(","))

    if (startX +startY)%2 == (endX - endY)%2 and max(startX, endX) <= r and max(startY, endY) <= c and min(startX, endX) >= 1 and min(startY, endY) >= 1:
        print("Yes")
    else:
        print("No")
