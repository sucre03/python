names=['lily','john','micle']
print(names[2],'will not come')
names[2]='sucre'
names.insert(0,'alice')
names.insert(2,'whsile')
names.append('lilei')
print('now,there are',len(names),'people')
print('Sorry!',names.pop())
print('Sorry!',names.pop())
print('Sorry!',names.pop())
print('Sorry!',names.pop())
print(names)
del names[0]
del names[0]
print(names)