for i in range(10):
    print(i,end=', ')
print('')

if 'exec_count' not in storage.keys():
    storage['exec_count'] = 0

for i in range(5):
    storage['exec_count'] = storage['exec_count'] + 1
print(storage)

print("Turning-Complete")

def contract_function():
    print('invoked contract_function')


if 'func' in kwargs:
    print(kwargs['func'])


