inp = open('Prob02.in.txt', 'r')

t = int(inp.readline())
v = ['a', 'e', 'i', 'o', 'u']
for _ in range(t):
    s = inp.readline()
    count = 0

    for x in s:
         if x in v:
             count += 1
    print(count)
    
