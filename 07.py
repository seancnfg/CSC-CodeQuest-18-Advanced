inp = open('Prob07.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    n = int(inp.readline())
    arr = []
    bad = []
    for __ in range(n):
        arr.append(inp.readline().strip())

    for i in range(len(arr)):
        x = arr[i].lower()
        if x != x[::-1]:
            bad.append(str(i + 1))
    if len(bad) >= 1:
        print("False -", ", ".join(bad))
    else:
        print("True")
