# Write a recursive function to calculate the sum of first n natural numbers.
'''
1 = 1
2 = 1 + 2
3 = 1 + 2 + 3
4 = 1 + 2 + 3 + 4
5 = 1 + 2 + 3 + 4 + 5
n = (n - 1) + n
'''
def sum(n):
    if (n == 1):
        return 1
    else:
        return sum(n-1) + n

print(sum(5))

