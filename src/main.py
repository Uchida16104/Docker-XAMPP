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
    xxx
except SystemError as e:
    print("SystemError")
    print(e)
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
