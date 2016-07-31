motocycles=['honda','yamaha','suzuki']
print(motocycles)
motocycles[0]='ducati'
print(motocycles)
motocycles.append('honda')
motocycles.insert(0,'ali')
print(motocycles)
del motocycles[0]
print(motocycles)
last_owned = motocycles.pop()
print('The last motorcycle I owned was a',last_owned)