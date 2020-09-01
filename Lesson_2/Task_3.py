# Task 3

month = int(input('choose a month '))

winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9, 10, 11]

if month in winter:
    print(month , ' месяц относится к зиме')
elif month in spring:
    print(month , ' месяц относится к весне')
elif month in summer:
    print(month, ' месяц относится к лету')
else:
    print(month, ' месяц относится к осени')

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)


