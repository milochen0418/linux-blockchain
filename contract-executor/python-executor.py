# This is python contract-executor
import os
def Execute(filename):
    #exec(compile(open(filename, "rb").read(), filename, 'exec'), globals, locals)
    #exec(compile(open(filename, "rb").read(), '<string>', 'exec')
    #exec(compile('print("Hello")'), '<string>', 'exec')
    pass
#Execute('./test_smart_contract.py')


execCodeObject = compile('a = 8; a = a + 10; print(a)', '<string>', 'exec')
executeCodeBlock = exec(execCodeObject)

filename = 'test_smart_contract.py'

QQ = open(filename,"rb").read()
print(QQ)

execCodeObject = compile(QQ, '<string>', 'exec')
executeCodeBlock = exec(execCodeObject)

