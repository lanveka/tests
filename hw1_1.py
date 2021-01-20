#v.4	По номеру месяца напечатать пору года.

y = int(input("Веедите номер месяца:\n"))
if y in range(3,6):
    print('Spring')
elif y in range(6,9):
    print('Summer')
elif y in range(9,12):
    print('Autumn')
elif y in range(1,3):
    print('Winter')
elif y == 12:
    print('Winter')
else:
    print('Wrong month number')