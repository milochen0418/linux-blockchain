# This is python contract-executor
import os
import pickle
import json 
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
contract_filename = 'contract.py'

def make_empty_storage():
    storage = {}
    python_object_dump(storage, storage_name)
    return storage
    pass

def Execute(filename, **kwargs):
    storage = python_object_load(storage_name)
    if storage == None:
        storage = make_empty_storage()
    
    readcode = open(filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec func=123')
    executeCodeBlock = exec(execCodeObject)
    python_object_dump(storage, storage_name)
    pass

def ExecuteFromJson(filename, jsonrpc):
    jsondict = json.loads(jsonrpc)
    print(jsondict['age'])


#Execute(contract_filename)
jsonrpc = '{ "name":"John", "age":30, "city":"New York"}'
ExecuteFromJson(contract_filename, jsonrpc)

exit(0)


