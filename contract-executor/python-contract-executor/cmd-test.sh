#!/bin/bash
python python-executor-without-web.py '{"func":"do_function_void" }'
python python-executor-without-web.py '{"func":"do_function_one_arg","arg1":"Hello World" }'
python python-executor-without-web.py '{"func":"func_with_args", "argNum":345,"argStr":"MyString"}'
python python-executor-without-web.py '{"func":"storage_setter","KeyStr":"OmgKey", "Value":3939889}'
python python-executor-without-web.py '{"func":"storage_getter","KeyStr":"OmgKey"}'
python python-executor-without-web.py '{"func":"storage_setter","KeyStr":"OmgKey", "Value":"Milo DApp"}'
python python-executor-without-web.py '{"func":"storage_getter","KeyStr":"OmgKey"}'
