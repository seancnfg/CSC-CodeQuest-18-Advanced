#Code still needs work
inp = open('Prob04.in.txt', 'r')

t = int(inp.readline())

for _ in range(t):
    arr = inp.readline().split()
    print(arr)
    rock = True
    scissors = True
    paper = True

    #if sorted(set(arr)) == ['P', 'R', 'S']:
     #   print("No Winner")
    #else:
    if 'R' in arr and 'S' in arr:
        scissors = False
    if 'S' in arr and 'P' in arr:
        paper = False
    if 'P' in arr and 'R' in arr:
        rock = False

    #print('rock', rock)
    #print('scissors', scissors)
    #print('paper', paper)

    if rock and paper and not scissors and 'R' in arr and 'P' in arr:
        print("PAPER")
    elif paper and scissors and not rock and 'P' in arr and 'S' in arr:
        print("SCISSORS")
    elif scissors and rock and not paper and 'S' in arr and 'R' in arr:
        print("ROCK")
    elif scissors and rock and 'P' not in arr:
        print("ROCK")
    else:
        print("NO WINNER")
