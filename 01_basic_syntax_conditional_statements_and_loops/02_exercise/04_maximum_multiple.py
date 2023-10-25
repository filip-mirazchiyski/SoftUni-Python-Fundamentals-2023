divisor = int(input())
boundary = int(input())
maxnum = 0

for i in range(1, boundary + 1):
    if i / divisor > 0 and i / divisor <= boundary and i % divisor == 0:
        maxnum = i
print(maxnum)