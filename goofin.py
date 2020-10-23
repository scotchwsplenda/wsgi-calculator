path = 'aaa.bbb.ccc.ddd.eee.fff.ggg'


path.split('.')
print(path.split('.')[2:])

args = [1,2,3,4,5]

amount = 0
sum = ""
for x in args:
    amount += x

sum = str(amount)

print(amount)
print(sum)  