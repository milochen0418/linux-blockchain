class SmartContract:
    def __init__(self):
        self.x = 33
        pass
    def do_function_void(self):
        print('do_function()')
    def do_function_one_arg(self,arg1):
        print('invoke do_function_one_arg({})'.format( arg1))


