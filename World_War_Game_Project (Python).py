hb = int(input('Enter Health Bar: '))
e = int(input('Enter No.Of Enemies: '))
p = 40
x1 = e // 4
x2 = p * x1
x3 = hb - x2
if x3 > 0:
    print('Remainning Health:',x3)
else:
    print('User Died')
