# This is python contract-executor
import os
def Execute(filename):
    exec(compile(open(filename, "rb").read(), filename, 'exec'), globals, locals)

Execute('./test_smart_contract.py')
