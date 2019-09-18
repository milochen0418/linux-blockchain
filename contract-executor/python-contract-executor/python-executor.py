# This is python contract-executor
import os
import pickle
import json
import sys
from shutil import copyfile


from threading import Thread
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import send_from_directory
from flask import request
flask_app = Flask(__name__)

class Env():
    DISABLE_FLASK_APP_LOG = False #Set true , then you will not see http post log

#Dssable flask log
if Env.DISABLE_FLASK_APP_LOG == True :
    import logging
    flask_app.logger.disabled = True
    log = logging.getLogger('werkzeug')
    log.disabled = True

flask_app.jinja_env.auto_reload = True
flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
import logging
flask_app.logger.disabled = True
@flask_app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@flask_app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js',path)

@flask_app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css',path)

@flask_app.route('/')
def index_page():
    return render_template('index.html')


storage_name = 'storage.bytes'
contract_filename = 'contract.py'
executable_contract_filename = 'exec_contract.py'


#jsonrpc = '{"func":"do_function_void" }'
#ExecuteFromJson(contract_filename, jsonrpc)

#, methods=['GET', 'POST']
@flask_app.route('/transaction', methods=['POST'])
def transaction_route():
    print('transaction_route() is invoked')
    try:
        if request.method == 'POST':
            #data = request.get_json()
            data = request.get_json(force=True)
            print('Data Received: "{data}"'.format(data=data))
            #print('type of data is ', type(data))
            #convert json data, with type of dict, into json str type.
            jsonrpc_str = json.dumps(data)
            #print('type of data is ', type(app_json))
            ExecuteFromJson(contract_filename, jsonrpc_str)
            return "Request Processed.\n"
    except Exception as e: 
        print(e)        
# curl localhost:5656/transaction -d '{"foo": "bar"}' -H 'Content-Type: application/json'

@flask_app.route('/post', methods=['POST'])
def post_route():
    print('post_route() is invoked')
    try:
        if request.method == 'POST':
            print('request.method == POST')
            #data = request.get_json()
            data = request.get_json(force=True)
            
            print('Data Received: "{data}"'.format(data=data))

            return "Request Processed.\n"
    except Exception as e: 
        print(e)        
# curl localhost:5656/post -d '{"foo": "bar"}' -H 'Content-Type: application/json'



@flask_app.route('/trans/<uid>')
def trans(uid):
    print('uid = ', uid)
    return ''

@flask_app.route('/trans2/')
def trans2():
    print('trans2() is invoked')
    if request.method == 'GET':
        print('this is get')
    elif request.method == 'POST':
        print('this is post')
    else:
        print('unknown request.method')
    
    return ''


@flask_app.route('/test/')
def test_page():
    return render_template('test.html')


class WebServerThread(Thread):
    global serverThread

    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            print('Flask web server start()')
            flask_app.jinja_env.auto_reload = True
            flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
            flask_app.run(host='0.0.0.0', port=5656, debug=False)
            print('Flask web server stop()')





def python_object_dump(obj, filename):
    file_w = open(filename, "wb")
    pickle.dump(obj, file_w)
    file_w.close()


def python_object_load(filename):
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

    # Procedure to load storage
    storage = python_object_load(storage_name)
    if storage == None:
        storage = make_empty_storage()
        
    # Convert jsonRPC str type into python dictionary
    jsondict = json.loads(jsonrpc)

    # Wrap the smart contract to be execuatable smart contract, 
    # so that it can be executed
    copyfile(filename, executable_contract_filename)
    exec_code = open(executable_contract_filename,"a+") #append
    exec_code.write("\ninst = SmartContract(storage)\n")
    if 'func' not in jsondict.keys():
        print('ExecuteFromJson: no func attribte')
        return 

    func = jsondict['func']
    arg_list = []
    for arg_name in jsondict.keys():
        if arg_name == 'func':
            continue
        arg_val = jsondict[arg_name]
        if type(arg_val) == str:
            readable_val = "'{}'".format(arg_val)
        else:
            readable_val = arg_val
        arg_list.append("{} = {}".format(arg_name, readable_val))
    arg_list_str = ""
    for v in arg_list:
        if arg_list_str == "":
            arg_list_str = v
        else:
            arg_list_str = "{},{}".format(arg_list_str, v)
    exec_code.write("inst.{}({})\n".format(func ,arg_list_str))
    exec_code.close()
    
    # To execute the executable smart contract
    readcode = open(executable_contract_filename,"rb").read()
    execCodeObject = compile(readcode, '<string>', 'exec')
    executeCodeBlock = exec(execCodeObject)
    
    # Procedure to save storage 
    python_object_dump(storage, storage_name)


# Test Code for python-executor.py with test contract contract.py
#jsonrpc = '{ "name":"John", "age":300, "city":"New York"}'
def run_test_case():
    jsonrpc = '{"func":"do_function_void" }'
    ExecuteFromJson(contract_filename, jsonrpc)
    jsonrpc = '{"func":"do_function_one_arg", "arg1":"Hello World" }'
    ExecuteFromJson(contract_filename, jsonrpc)
    jsonrpc = '{"func":"func_with_args", "argNum":345, "argStr":"MyString"}'
    ExecuteFromJson(contract_filename, jsonrpc)
def run_contract_by_jsonrpc(jsonrpc):
    ExecuteFromJson(contract_filename, jsonrpc)

if __name__=="__main__":
    #run_test_case()
    #print(sys.argv)
    if len(sys.argv) == 1:
        run_test_case()
    elif len(sys.argv) == 2:
        run_contract_by_jsonrpc(sys.argv[1])
        # To refer cmd example, you can read the code in  cmd-test.sh

    Web_ServerThread = WebServerThread()
    Web_ServerThread.start()
    print('Browser open http://localhost:5656/ . It\'s mapping to template/index.html')
    print('Browser open http://localhost:5656/test/ . It\'s mapping to template/test.html')
    #sys.exit(flask_app.exec_())
    
    #exit(0)


