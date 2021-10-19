v1, v2, t, s, l = map(int, "4 2 2 2 12".split())
i = 0
S1 = 0
S2 = 0
j = 0

while S1 < l and S2 < l:
    if S1 - S2 >= t:
        S1 = v1 * i
        S2 = v2 * (i + s)
        i = i + t
        j = j + 1
    else:
        i = i + 1
        S1 = v1 * (i - j * s)
        S2 = v2 * i

if S1 > S2:
    print('T')
elif S1 < S2:
    print('R')
else:
    print('D')

# input: 2 2 0 0 10   output: D 5
# input: 4 2 2 2 12   output: R 5
# input: 4 1 2 2 12   output: R 9
# input: 2 3 2 2 12   output: T 4
