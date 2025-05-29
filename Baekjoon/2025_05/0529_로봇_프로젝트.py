# BOJ 3649
import sys

for line in sys.stdin:
    try:
        x = int(line.strip()) * 10**7
        n = int(sys.stdin.readline())
        l = [int(sys.stdin.readline()) for _ in range(n)]

        l.sort()
        left = 0
        right = n - 1
        found = False

        while left < right:
            total = l[left] + l[right]
            if total == x:
                print("yes", l[left], l[right])
                found = True
                break
            elif total < x:
                left += 1
            else:
                right -= 1

        if not found:
            print("danger")
    except:
        break
