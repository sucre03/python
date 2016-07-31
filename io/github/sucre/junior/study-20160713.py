# enum
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
'''
The special attribute __members__ is an ordered dictionary mapping names to members.
It includes all names defined in the enumeration, including the aliases:
'''
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# Enum class decorator that ensures only one name is bound to any one value.

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tus = 2
    Wen = 3
    Thr = 4
    Fir = 5
    Sat = 6
print(Weekday.Sun,Weekday.Sun.value)