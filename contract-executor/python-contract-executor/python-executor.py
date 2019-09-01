# This is python contract-executor
import os
def Execute(filename):
    readcode = open(filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec')
    executeCodeBlock = exec(execCodeObject)
    pass

Execute('./test_smart_contract.py')
Execute('./test_smart_contract.py')
exit(0)


