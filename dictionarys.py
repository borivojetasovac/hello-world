#!/usr/bin/python3
import pprint

birthdays = {'Alice': 'Apr 1', 'Carol': 'Mar 4', 'Bob': 'Dec 12'}
birthdays2 = {'Alice': 'Apr 1', 'Carol': 'Mar 4', 'Bob': 'Dec 12'}
print(birthdays['Alice'])
print(birthdays == birthdays2)          # True - items are unordered

while True:
    name = input('Enter a name (or enter to finish): ')
    if name == '':
        print('')
        break
    if name in birthdays:
        print(name + "'s birthday is: " + birthdays[name])
    else:
        date = input('What is their birthday? ')
        birthdays[name] = date
        print('Birthdays database updated.')

# Multiple assignment:      returns list-like values: keys(), values() and items()
for k, v in birthdays.items():
    print(k + "'s birthday is: " + v)
print('')

print("Ana's birthday is " + birthdays.get('Ana', 'not anounced.'))  # if Ana doesn't exist in keys, 'not anounced' will be returned
birthdays.setdefault('Ana', 'Feb 15')   # if the key 'Ana' doesn't exsits - it adds this key-value pair, if it does - it returns the key's value

pprint.pprint(birthdays)                # sorts everything by keys, and adds new lines if needed
# print(pprint.pformat(count))  - equivalent to the line above (pformat if you want to obtain formated text as a string)
