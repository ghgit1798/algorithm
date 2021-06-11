import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

# N이 K 이상이라면 k로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)