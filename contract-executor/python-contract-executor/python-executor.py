# This is python contract-executor
import os
import pickle

def python_object_dump(obj, filename):
    import os
    import time
    import pickle
    file_w = open(filename, "wb")
    pickle.dump(obj, file_w)
    file_w.close()


def python_object_load(filename):
    import os
    import time
    import pickle
    file_r = open(filename, "rb")
    obj2 = pickle.load(file_r)
    file_r.close()
    return obj2
storage = None

def make_empty_storage():
    storage = {}
    python_object_dump(storage, 'storage.bytes')
    pass

def Execute(filename):
    readcode = open(filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec')
    executeCodeBlock = exec(execCodeObject)
    pass


make_empty_storage()
Execute('./test_smart_contract.py')
Execute('./test_smart_contract.py')
exit(0)


