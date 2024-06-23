#method 3:
#complexity --> O(n)
#using recursion

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

n = 5
print(sum(n))
