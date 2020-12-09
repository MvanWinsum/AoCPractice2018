code = [line.rstrip() for line in open('puzzle_input.txt')]

a, ip = 0, 0
maybe_bugs, history = [], []
while ip not in history:
    history.append(ip)
    c, sv = code[ip].split()
    if c == 'acc':
        a += int(sv)
        ip += 1
    elif c == 'jmp':
        maybe_bugs.append(ip)
        ip += int(sv)
    elif c == 'nop':
        maybe_bugs.append(ip)
        ip += 1
print("Part 1: acc=", a)

for bug in maybe_bugs:
    a, ip = 0, 0
    history = []
    while ip not in history and ip < len(code):
        history.append(ip)
        c, sv = code[ip].split()
        if ip == bug:
            if c == 'jmp':
                c = 'nop'
            else:
                c = 'jmp'
        if c == 'acc':
            a += int(sv)
            ip += 1
        elif c == 'jmp':
            ip += int(sv)
        elif c == 'nop':
            ip += 1

    if ip == len(code):
        print(f"Part 2: bugline={bug} ({code[bug]}) acc={a}")
        break