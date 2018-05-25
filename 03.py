inp = open('Prob03.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    s = inp.readline().strip()

    number = s[0:-2]

    if number[-1] == "1" and len(number) != 2:
        print(number + "st")
    elif number[-1] == "2" and len(number) != 2:
        print(number + "nd")
    elif number[-1] == "3" and len(number) != 2:
        print(number + "rd")
    else:
        print(s)
