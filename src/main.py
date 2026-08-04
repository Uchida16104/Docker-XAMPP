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
