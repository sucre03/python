alien_color = 'green'

if alien_color == 'green':
    print('You win five starts')
elif alien_color != 'green':
    print('You win ten starts')
else:
    print('You win fifty starts')

age = 30
if age < 2:
    print('you are baby')
elif age >= 2 and age < 4:
    print('学步')
elif age >=4 and age <13:
    print('children')
elif age >=13 and age <20:
    print('younger')
elif age >=20 and age <65:
    print('成年')
elif age >= 65:
    print('老年人')

fruits = ['apple','banana','pear','grape','watermelon']
if 'banana' in fruits:
    print('you really like bananas!')
if 'tomato' not in fruits:
    print('oh!no')
if fruits:
    print('have many fruits')
else:
    print('空的')
