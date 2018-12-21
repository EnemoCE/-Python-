#февраль легко проверить!
import calendar
dat = input('Введите дату: ')
dat = dat.split('.')
r1 = dat[0]
r2 = dat[1]
r3 = dat[2]
k = len(r1) == 2 and len(r2) == 2 and len(r3) == 4
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)
if k and (0 < r2 < 13) and (0 < r3 < 9999 ) :
    days = list(calendar.monthrange(r3,r2))
    days = days[1]
    if 0 < r1 <= days :
        print('Дата введена корректно')
    else :
        print('Дата введена некорректно')
else:
    print('Дата введена некорректно')
