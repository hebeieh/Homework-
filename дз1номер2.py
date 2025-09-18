column_number = int(input())
result = []
while column_number > 0:
    column_number -= 1
    num = column_number % 26
    result.append(chr(65 + num))
    column_number //= 26
title = ''.join(result[::-1])
print(title)