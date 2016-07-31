cars = ['bmw', 'toyota', 'audi', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'toyota', 'audi', 'subaru','dazhong','buick']

print('临时修改',cars)
#临时修改
print(sorted(cars))
print(sorted(cars,reverse=True))
print(cars)
#反转
cars.reverse()
print(cars,len(cars))
