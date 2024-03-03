n, k = map(int, input().split())
if n < k:
    print('Первому повезло меньше')
elif k < n:
    print('Второму повезло меньше')
else:
    print('Одинаковый улов')
