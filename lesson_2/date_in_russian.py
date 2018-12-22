import datetime
import pytils
str = input('¬ведите дату в виде dd.mm.yyyy: ')
str = str.split('.')
str = [int(k) for k in str]
n1 = str[2]
n2 = str[1]
n3 = str[0]
dataru = pytils.dt.ru_strftime(u"%d %B %Y", inflected=True, date=datetime.date(n1,n2,n3))
print(dataru)
