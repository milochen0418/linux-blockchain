class SmartContract:
    def __init__(self, storage):
        self.x = 33
        self.storage = storage
        pass
    def do_function_void(self):
        print('do_function()')
        if 'cnt' not in self.storage.keys():
            self.storage['cnt'] = 0
        else:
            self.storage['cnt'] += 1
    def do_function_one_arg(self,arg1):
        print('invoke do_function_one_arg({})'.format( arg1))


