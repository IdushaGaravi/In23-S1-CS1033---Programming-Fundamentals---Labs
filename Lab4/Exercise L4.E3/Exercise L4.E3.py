# Exercise L4.E3

msg = input('Enter message: ')
base = int(input('Enter base: '))
lst=[]
for i in list(msg):
    lst.append(ord(i))
for number in lst:
    result = ''
    while number > 0:
        result = str(number % base) + result
        number //= base
    print(result, end='')
