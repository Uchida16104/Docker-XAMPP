print("Hello world!")
a = 5; b = 3; c = a + b
print(c)
total = 123 \
      + 456 \
      + 789
months = [ 'Jan', 'Feb', 'Mar', 'Apr',
           'May', 'Jun', 'Jul', 'Aug',
           'Sep', 'Oct', 'Nov', 'Dec' ]
a = 3
if a == 5:
    print("AAA")
    print("BBB")
print("CCC")
print(3)
print([1, 2, 3])
print((1, 2, 3))
print({'k1':10, 'k2':20})
print("AAA", "BBB")
print("AAA", end="")
print("BBB")
print("My name is %s." % "Tanaka")
print("%s is %d years old." % ("Tanaka", 28))
print("%(name)s is %(age)d years old." % {'name': "Tanaka", 'age': 28})
num = 1234
num = 0b11000100
num = 0o777
num = 0xffff
num = 1_234_567_890
num = 1.234
num = 1.2e3
num = 1.2E-3
num = 3.14j
bool = True
bool = False
x = None
str = "Hello world"
str = 'Hello world'
str = "We can use ' in the double quotation string."
str = 'We can use " in the single quotation string.'
str = "We can use \" in the string."
str = 'We can use \' in the string.'
str = 'aaa\nbbb'
str = r'aaa\nbbb'
name = "Yamada"
age = 26
print(f"My name is {name}. I'm {age} years old.")
print(f"{{n}}")
s = "ABC"
print(f"|{s}|")
print(f"|{s:<9}|")
print(f"|{s:^9}|")
print(f"|{s:>9}|")
n = 12345
print(f"{n:,}")
n = 123
print(f"{n}")
print(f"{n:b}")
print(f"{n:o}")
print(f"{n:x}")
print(f"{n:X}")
a = 123
b = -123
print(f"{a:+} {b:+}")
print(f"{a:-} {b:-}")
print(f"{n:#}")        
print(f"{n:#b}")       
print(f"{n:#o}")       
print(f"{n:#x}")       
print(f"{n:#X}")       
print(f"{n:08}")       
print(f"{n:08b}")      
print(f"{n:08o}")      
print(f"{n:08x}")      
print(f"{n:08X}")      
n = 12.3456
print(f"{n:.2f}")      
print(f"{n:8.2f}")     
print(f"{n:.2e}")      
print(f"{n:.2E}")      
print(f"{n:.2g}")      
print(f"{n:.2%}")      
name = "Yamada"
age = 36
print(f"{name=}, {age=}")
byte_string = b"\xe3\x81\x82"
utf8_string = byte_string.decode()
print(utf8_string)
utf8_string = "あ"
byte_string = utf8_string.encode()
print(byte_string)
utf8_str = "あ"
utf8_bytes = utf8_str.encode('utf-8')
sjis_bytes = utf8_str.encode('sjis')
cp932_bytes = utf8_str.encode('cp932')
eucjp_bytes = utf8_str.encode('euc_jp')
jis_bytes = utf8_str.encode('iso2022_jp')
utf8_str = utf8_bytes.decode('utf-8')
utf8_str = sjis_bytes.decode('sjis')
utf8_str = cp932_bytes.decode('cp932')
utf8_str = eucjp_bytes.decode('euc_jp')
utf8_str = jis_bytes.decode('iso2022_jp')
# coding: utf-8
print(len("あいうえお"))
print(len(u"あいうえお"))
str = """A simple example module
This module is ...
"""
str = "Hello \
world!"
print("Hello " "world!")
print("%s" % "ABC")
print("%d" % 123)
print("%f" % 1.23)          
print("%x" % 255)           
print("%o" % 255)           
print("%%%d" % 80)          
print("|%5s|" % 'ABC')      
print("|%-5s|" % 'ABC')      
print("|%5d|" % 123)         
print("|%-5d|" % 123)        
print("|%+5d|" % 123)        
print("|%5.2f|" % 1.23)      
print("|%05d|" % 123)
value1 = 123
_value1 = 123
test_value = 123
TEST_VALUE = 123
PI = 3.14
MAX_BUFFER_SIZE = 1024
"""A sample module"""
class MyClass:
    """A sample class"""
    def myfunc(self, x, y):
        """A sample function"""
        return x + y
a = [10, 20, 30, 40]
colors = [
    'red',
    'green',
    'blue',
]
a = [10, 'ABC']
a = [1, 2, 3, 4, 5]
for n in a:
    print(n)
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
a1 = a[0]
a2 = a[2]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = a[2:4]
a2 = a[2:]
a3 = a[:4]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = a[1:8:2]
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
a1 = a[-1]
a2 = a[-3:-1]
print([1, 2, 3] + [4, 5, 6])
print(len([1, 2, 3]))
a = [[1, 2], [3, 4], [5, 6]]
for list in a:
    for n in list:
        print(n)
a = (10, 20, 30, 40)
a = (10)
a = (10,)
a1 = [10, 20, 30, 40]
a2 = (10, 20, 30, 40)
a1[2] = 60
print(tuple([1, 2, 3]))
def get_date():
    return 2022, 10, 9
year, month, day = get_date()
print("%04d/%02d/%02d" % (year, month, day))
d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}
d1 = d['Yamada']
d2 = d['Suzuki']
d3 = d['Tanaka']
d['Kimura'] = 60
d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}
for k, v in d.items():
    print(k, v)
for k in d.keys():
    print(k, d[k])
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)
a = [1, 2, 3]
def double(x): return x * 2
print([x * 2 for x in a])
a = [1, 2, 3]
def isodd(x): return x % 2
print([x for x in a if x % 2])
a = [1, 2, 3]
print([x * 2 for x in a])
print([x * 2 for x in a if x == 3])
print([[x, x * 2] for x in a])
print([(x, x * 2) for x in a])
b = [4, 5, 6]
print([x * y for x in a for y in b])
print([a[i] * b[i] for i in range(len(a))])
a = set(['red', 'blue', 'green'])
b = set(['green', 'yellow', 'white'])
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print('green' in a)
a.add('black')
print(a)
err = 0
print("OK" if err == 0 else "NG")
s = "ABCDEF"
if (len := len(s)) > 5:
    print("LONG")
else:
    print("SHORT")
num = 12
if num > 10:
    print("BIG")
    print("BIG")
    print("BIG")
num = 12
if num > 10:
    print("BIG")
else:
    print("SMALL")
num = 12
if num > 10:
    print("BIG")
elif num == 10:
    print("NORMAL")
else:
    print("SMALL")
n = 0
while n < 10:
    print(n)
    n += 1
n = 0
while n < 10:
    print(n)
    n += 1
else:
    print('END')
for n in [1, 2, 3]:
    print(n)
for n in (1, 2, 3):
    print(n)
for c in "ABC":
    print(c)
for k in {'one': 1, 'two': 2, 'three': 3}:
    print(k)                                
for n in [1, 2, 3]:
    print(n)
else:
    print('END')
for n in range(10):
    print(n)
for n in range(10):
    if n == 5:
        break
    print(n)
    if n == 5:
        continue
    print(n)
str = 'ABC'
try:
    c = str[5]
except IOError:
    print('IOError')
except IndexError:
    print('IndexError')
except:
    print('Unknown')
else:
    print('Other')
finally:
    print('Finally')
try:
    raise SystemError('Error message')
except SystemError as e:
    print("SystemError")
    print(e)
except Exception as e:
    raise e
except Exception:
    raise MyError()
except Exception as e:
    raise MyError() from e
except Exception:
    raise MyError() from None
def myfunc():
    pass
class MyClass:
    pass
x = 5
y = [1, 2, 3]
z = MyClass()
del x, y, z
exec("print('Hello')")
exec("print(global_x, local_y)", {'global_x': 100}, {'local_y': 200})
c = 3
match c:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")
def add(x, y):
    print(x + y)
add(3, 5) 
def add(x, y):
    ans = x + y
    return ans
n = add(3, 5)
print(n)
def func():
    return 3, "ABC"
n, s = func()
print(n, s)
def repeat_msg(msg, repeat=3):
    for i in range(repeat):
        print(msg)
repeat_msg('Hello')
repeat_msg('Yahho', repeat=5)
def func(a, b, *, c):
   print("a=%s, b=%s, c=%s" % (a, b, c))
func("A", "B", c="C")
def func(a, b, /, c):
   print("a=%s, b=%s, c=%s" % (a, b, c))
func("A", "B", "C")
func("A", "B", c="C")
def func(a1, a2, *args, **kwargs):
    print(a1)
    print(a2)
    print(args)
    print(kwargs)
func('A', 'B', 'C', 'D', k1='K1', k2='K2')
def func(a1, a2, *args, **kwargs):
    print(a1)                    
    print(a2)                    
    print(args)                  
    print(kwargs)                
args = ('C', 'D')
kwargs = {'k1': 'K1', 'k2': 'K2'}
func('A', 'B', *args, **kwargs)
def func(x, y):
    """A sample function"""
    return x + y
count = 0
def func1():
    print(count)
def func2():
    global count
    count += 1
def func():
    for k in globals().keys():
        print("GLOBAL: %s = %s" % (k, globals()[k]))
    for k in locals().keys():
        print("LOCAL: %s = %s" % (k, locals()[k]))
func()
count = 999
def counter():
    count = 0             
    def count_up():
        nonlocal count    
        count += 1
        return count
    return count_up

cnt = counter()
print(cnt())              
print(cnt())              
myfunc = lambda x, y: x + y
print(myfunc(3, 5))
a = [1, 2, 3]
print(list(map(lambda x: x ** 2, a)))
class MyRange:
    def __init__(self, max):
        self._max = max

    def __iter__(self):
        self._count = 0
        return self
    def __next__(self):
        result = self._count
        if result >= self._max:
            raise StopIteration
        self._count += 1
        return result
for n in MyRange(5):
    print(n)
print(cnt())
def funcA(list):
    ret = []
    for n in list:
        ret.append(n * 2)
    return ret
for n in funcA([1, 2, 3, 4, 5]):
    print(n)
def funcB(list):
    for n in list:
        yield n * 2
for n in funcB([1, 2, 3, 4, 5]):
    print(n)
def mydecolater(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
@mydecolater
def hello():
    print("hello")
hello() 
def mydecolater(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Funcname:", func.__name__)
        print("Arguments:", args)
        print("Keywords:", kwargs)
        ret = func(*args, **kwargs)
        print("Return:", ret)
        return ret
    return wrapper
@mydecolater
def func(msg1, msg2, flag=1, mode=2):
    """A sample function"""
    print("----", msg1, msg2, "----")
    return 1234
n = func("Hello", "Hello2", flag=1)
print(n)
print(repr(func))
print(func.__doc__)
class MyClass:
    """A simple example class"""
    def __init__(self):
        self.name = ""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
a = MyClass()
a.setName("Tanaka")
print(a.getName())
class MyClass:
    def __init__(self):
        self.name = ""
a1 = MyClass()
a1.name = "Tanaka"

a2 = MyClass()
a2.name = "Suzuki"
print(a1.name)
print(a2.name)
class MyClass:
    PI = 3.14
print(MyClass.PI)
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1
a1 = MyClass()
a2 = MyClass()
print(MyClass.count)
class MyClass:
    pass
a1 = MyClass()
a1.name2 = "Tanaka"
MyClass.PI2 = 3.141593
class MyClass:
    PI = 3.14
a1 = MyClass()
a2 = MyClass()
print(a1.PI)
a1.PI = 3.141593
print(a1.PI)
print(a2.PI)
class MyClass:
    name = ""
    def setName(self, name):
        self.name = name
a = MyClass()
a.setName("Tanaka")
class MyClass:
    def __init__(self):
        self.name = "tanaka"
        self._name = "yamada"
        self.__name = "suzuki"

    def hello(self): print('hello')
    def _hello(self): print('hello')
    def __hello(self): print('hello')
a = MyClass()
print(a.name)
a.hello()
print(a._MyClass__name)
a._MyClass__hello()
class MyClass:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
a = MyClass("Tanaka")
print(a.getName())
class MyClass:
    def __init__(self):
        print("INIT!")
    def __del__(self):
        print("DEL!")
a = MyClass()
del a
class MyClass:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name
a = MyClass("Yamada")
print(a)
class MyClass:
    def hello(self):
        print("Hello")
class MyClass2(MyClass):
    def world(self):
        print("World")
a = MyClass2()
a.hello()
a.world()
class MyClass:
    def hello(self):
        print("Hello")
class MyClass2(MyClass):
    def hello(self):
        print("HELLO")
a = MyClass2()
a.hello()
class MyClass1(object):
    def __init__(self):
       self.val1 = 123
class MyClass2(MyClass1):
    def __init__(self):
        super(MyClass2, self).__init__()
        self.val2 = 456
a = MyClass2()
print(a.val1)
print(a.val2)
class MyClassA:
    def funcA(self):
        print("MyClassA:funcA")
class MyClassB:
    def funcB(self):
        print("MyClassB:funcB")
class MyClassC(MyClassA, MyClassB):
    pass
a = MyClassC()
a.funcA()
a.funcB()
