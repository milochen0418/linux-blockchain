# This is python contract-executor
import os
import pickle
import json
import inspect
import time
from shutil import copyfile
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
executable_contract_filename = 'exec_contract.py'

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

def end_of_read_contract():
    print('call end of read contract()')
    contract_instance = SmartContract() 
    #f = getattr(contract_instance, 'do_function_void')
    #f()
    pass
 
def ExecuteFromJson(filename, jsonrpc):
    storage = python_object_load(storage_name)
    if storage == None:
        storage = make_empty_storage()
    Source_end_of_read_contract = inspect.getsource(end_of_read_contract)
    jsondict = json.loads(jsonrpc)
    
    copyfile(filename, executable_contract_filename)
    exec_code = open(executable_contract_filename,"a+") #append

    exec_code.write("\ninst = SmartContract()\n")
    exec_code.write("inst.{}()\n".format(jsondict['func']))

    exec_code.close()
    

    readcode = open(executable_contract_filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec')
    executeCodeBlock = exec(execCodeObject)

#Execute(contract_filename)
#jsonrpc = '{ "name":"John", "age":300, "city":"New York"}'

jsonrpc = '{"func":"do_function_void" }'
ExecuteFromJson(contract_filename, jsonrpc)
jsonrpc = '{"func":"do_function_void" }'

exit(0)


