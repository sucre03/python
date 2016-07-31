[print(value) for value in range(1, 21)]
# nums = [print(value) for value in range(1,1000000)]
nums = list(range(1, 1000000))
print(min(nums), max(nums), sum(nums))

odd_nums = [print('奇数为',value) for value in range(1,20,2)]
threes = [print('3的倍数为',value) for value in range(3,30,3)]
cube = [print('立方为',value**3) for value in range(1,11)]
list = list(range(1,10))
print('The first three items in the list are:',nums[:3])
print('Three items from the middle of the list are:',list[3:6])
print('The last Three items in the list are:',list[6:])


my_foods = ['pizza','falafel','carrot cake']
friend_pizzas = my_foods
my_foods.append('bisk')
friend_pizzas.append('deks')
print('My favorite pizzas are:',my_foods)
print("My friend's favorite pizzas are:",friend_pizzas)