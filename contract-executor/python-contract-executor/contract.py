
"""
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
"""


#for key in kwargs.keys():
#    print(key,'->',kwargs[key])
class SmartContract:
    def __init__(self):
        self.x = 33
        pass
    def do_function_void(self):
        print('do_function()')
    def do_function_one_arg(self,arg1):
        print('invoke do_function_one_arg({})'.format( arg1))

def end_of_read_contract():
    print('call end of read contract()')
    contract_instance = SmartContract()
    #f = getattr(contract_instance, 'do_function_void')
    #f()
    pass
 

end_of_read_contract()


