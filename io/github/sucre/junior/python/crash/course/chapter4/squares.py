squares = []
for value in range(1,10):
    squares.append(value**2)
print(squares)
print('max num is',max(squares),',min num is',min(squares),'and sum is',sum(squares))

squares_great = [value**2 for value in range(1,11)]
print(squares_great)