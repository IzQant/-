input = __import__('sys').stdin.readline

n = int(input()) #출입 기록 수
people = set()
for _ in range(n):
    a, b = map(str, input().split())
    if a not in people and b == 'enter':
        people.add(a)
    if a in people and b == 'leave':
        people.remove(a)
people = sorted(people, reverse = True)
print('\n'.join(people))