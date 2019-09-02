import os
for i in range(10):
    print(i)
if 'exec_count' not in storage.keys():
    storage['exec_count'] = 0
storage['exec_count'] = storage['exec_count'] + 1

print(storage)

