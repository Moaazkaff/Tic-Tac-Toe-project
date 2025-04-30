import math

def minmax(depth ,  index , table , is_maximizing_player , h , n):
    if index >= n:
        return -math.inf if is_maximizing_player else math.inf
    if depth == h or (index * 2) + 1 >= n:
        return table[index]
    if is_maximizing_player:
        left = minmax(depth + 1 , index * 2 + 1, table, False, h, n) 
        right = minmax(depth + 1 , index *2 + 2 , table , False , h , n)
        return max(left , right)
    else:
        left = minmax(depth + 1 , index * 2 + 1, table, True, h, n) 
        right = minmax(depth + 1 , index *2 + 2 , table , True , h , n)
        return min(left , right)

def log2(n):
    return 0 if n == 1 else 1 + log2(n // 2)

# table = [3, 5, 2, 9, 12, 5, 23, 23]
# table = [7, 13, 5, 10, 8, 4, 6, 2]
table = [3, 5, 2, 9, 12]
n = len(table)
h = log2(n)
print("The optimal value is: ", minmax(0, 0, table, True, h, n))