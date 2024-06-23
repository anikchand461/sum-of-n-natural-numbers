#method 1:
#complexity --> O(n)

def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = 5
print(sum(5))
