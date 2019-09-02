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
    try:
        file_r = open(filename, "rb")
        obj2 = pickle.load(file_r)
        file_r.close()
    except:
        try:
            file_r.close()
            return None
        except:
            return None
    return obj2
storage_name = 'storage.bytes' 
def make_empty_storage():
    storage = {}
    python_object_dump(storage, storage_name)
    return storage
    pass

def Execute(filename):
    storage = python_object_load(storage_name)
    if storage == None:
        storage = make_empty_storage()
    
    readcode = open(filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec')
    executeCodeBlock = exec(execCodeObject)
    python_object_dump(storage, storage_name)

    pass


Execute('./test_smart_contract.py')


exit(0)


