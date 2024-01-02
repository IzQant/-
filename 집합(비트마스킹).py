#비트마스킹 사용
import sys

N = int(sys.stdin.readline())
S = 0
for _ in range(N):
    order = sys.stdin.readline()
    try:
        op, x = order.split()
        x = int(x)
        if 'add' in order:
            S |= (1 << x)
        elif 'remove' in order:
            S &= ~(1 << x)
        elif 'check' in order:
            print(1 if S & (1 << x) != 0 else 0)
        elif 'toggle' in order:
            S ^= (1 << x)

    except:
        if 'all' in order:
            S = (1 << 21) -1
        elif 'empty' in order:
            S = 0
