class SmartContract:
    def __init__(self, storage):
        self.storage = storage
        pass

    def do_function_void(self):
        print('do_function_void()')
        if 'cnt' not in self.storage.keys():
            self.storage['cnt'] = 0
        else:
            self.storage['cnt'] += 1
        # show storage data
        print(self.storage)

    def do_function_one_arg(self,arg1):
        print('invoke do_function_one_arg({})'.format( arg1))

    def func_with_args(self, argNum, argStr):
        print('argNum = ', argNum)
        print('argStr = ', argStr)

    def storage_setter(self, KeyStr, Value):
        self.storage[KeyStr] = Value
        print('set done')
    def storage_getter(self, KeyStr):
        print('get ', self.storage[KeyStr])


