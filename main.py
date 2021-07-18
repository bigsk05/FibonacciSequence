import os,threading,shutil,json,time

source="code"
def testc():
    shutil.copy(source+"/c.c","tmp/c.c")
    time.sleep(1)
    os.popen("gcc tmp/c.c -o tmp/testc")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("./tmp/testc").read())[0]
        print("C completed once used {}s".format(value))
        result.append(value)
    print("C completed all tasks used {}s".format(sum(result)))
    with open("rec/c.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testcpp():
    shutil.copy(source+"/cpp.cpp","tmp/cpp.cpp")
    time.sleep(1)
    os.popen("g++ tmp/cpp.cpp -o tmp/testcpp")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("./tmp/testcpp").read())[0]
        print("C++ completed once used {}s".format(value))
        result.append(value)
    print("C++ completed all tasks used {}s".format(sum(result)))
    with open("rec/cpp.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testjava():
    shutil.copy(source+"/java.java","tmp/java.java")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("java tmp/java.java").read())[0]
        print("Java completed once used {}s".format(value))
        result.append(value)
    print("Java completed all tasks used {}s".format(sum(result)))
    with open("rec/java.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testgo():
    shutil.copy(source+"/go.go","tmp/go.go")
    time.sleep(1)
    os.popen("go build -o tmp/go tmp/go.go")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("./tmp/go").read())[0]
        print("Go completed once used {}s".format(value))
        result.append(value)
    print("Go completed all tasks used {}s".format(sum(result)))
    with open("rec/go.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testjs():
    shutil.copy(source+"/javascript.js","tmp/javascript.js")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("node tmp/javascript.js").read())[0]
        print("Node completed once used {}s".format(value))
        result.append(value)
    print("Node completed all tasks used {}s".format(sum(result)))
    with open("rec/node.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testlua():
    shutil.copy(source+"/lua.lua","tmp/lua.lua")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("lua tmp/lua.lua").read())[0]
        print("Lua completed once used {}s".format(value))
        result.append(value)
    print("Lua completed all tasks used {}s".format(sum(result)))
    with open("rec/lua.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testlua():
    shutil.copy(source+"/lua.lua","tmp/lua.lua")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("lua tmp/lua.lua").read())[0]
        print("Lua completed once used {}s".format(value))
        result.append(value)
    print("Lua completed all tasks used {}s".format(sum(result)))
    with open("rec/lua.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testperl():
    shutil.copy(source+"/perl.pl","tmp/perl.pl")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("perl tmp/perl.pl").read())[0]
        print("Perl completed once used {}s".format(value))
        result.append(value)
    print("Perl completed all tasks used {}s".format(sum(result)))
    with open("rec/perl.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testphp():
    shutil.copy(source+"/php.php","tmp/php.php")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("php tmp/php.php").read())[0]
        print("PHP completed once used {}s".format(value))
        result.append(value)
    print("PHP completed all tasks used {}s".format(sum(result)))
    with open("rec/php.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testR():
    shutil.copy(source+"/R.R","tmp/R.R")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("./tmp/R.R").read()[5:-2])[0]
        print("R completed once used {}s".format(value))
        result.append(value)
    print("R completed all tasks used {}s".format(sum(result)))
    with open("rec/R.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testruby():
    shutil.copy(source+"/ruby.rb","tmp/ruby.rb")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("ruby tmp/ruby.rb").read())[0]
        print("Ruby completed once used {}s".format(value))
        result.append(value)
    print("Ruby completed all tasks used {}s".format(sum(result)))
    with open("rec/ruby.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testpython2():
    shutil.copy(source+"/python.py","tmp/python2.py")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("python tmp/python2.py").read())[0]
        print("Python2 completed once used {}s".format(value))
        result.append(value)
    print("Python2 completed all tasks used {}s".format(sum(result)))
    with open("rec/python2.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testpython3():
    shutil.copy(source+"/python.py","tmp/python3.py")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("python3 tmp/python3.py").read())[0]
        print("Python3 completed once used {}s".format(value))
        result.append(value)
    print("Python3 completed all tasks used {}s".format(sum(result)))
    with open("rec/python3.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testpypy():
    shutil.copy(source+"/python.py","tmp/pypy.py")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("pypy tmp/pypy.py").read())[0]
        print("Pypy completed once used {}s".format(value))
        result.append(value)
    print("Pypy completed all tasks used {}s".format(sum(result)))
    with open("rec/pypy.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def testjython():
    shutil.copy(source+"/python.py","tmp/jython.py")
    time.sleep(1)
    result=[]
    for i in range(0,100):
        value=json.loads(os.popen("jython tmp/jython.py").read())[0]
        print("Jython completed once used {}s".format(value))
        result.append(value)
    print("Jython completed all tasks used {}s".format(sum(result)))
    with open("rec/jython.txt","a+") as fb:
        fb.write(json.dumps(result))
        fb.write("\nTotally used:{} Average:{}".format(sum(result),sum(result)/len(result)))
        fb.write("\n----------------\n")
def t1():
    testcpp()
    testjava()
    testgo()
    testlua()
    testjython()
    testperl()
    testjs()
def t2():
    testphp()
    testR()
    testruby()
    testpython2()
    testc()
    testpython3()
    testpypy()
    testperl()
def main():
    os.makedirs("rec",exist_ok=True)
    try:
        shutil.rmtree("tmp")
    except:
        pass
    os.makedirs("tmp")
    #threading.Thread(target=t1).start()
    #threading.Thread(target=t2).start()
    input()
    testgo()
    testlua()
    testjython()
    testperl()
    testjs()
main()
