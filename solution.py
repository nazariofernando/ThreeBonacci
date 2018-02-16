def tribonnaci(first, second, third):
    return third+second-first

fi = open('./input.txt', 'r')
inp = fi.read().split()

first = int(inp[0])
second = int(inp[1])
third = int(inp[2])
term = int(inp[3])

solution = 0

if term == 0:
    solution = first
elif term == 1:
    solution = second
elif term == 2:
    solution = third
else:
    for x in range(0, term-2):
        solution = tribonnaci(first, second, third)
        first = second
        second = third
        third = solution

fo = open('./output.txt', 'w')
fo.write(str(solution))
