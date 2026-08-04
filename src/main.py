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
num = 9223372036854775808L
num = 1234567890123456789012345678901234567890123456789012345678901234567890L
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
print(f"{n:#}")        # 123
print(f"{n:#b}")       # 0b1111011
print(f"{n:#o}")       # 0o173
print(f"{n:#x}")       # 0x7b
print(f"{n:#X}")       # 0X7B
print(f"{n:08}")       # 00000123
print(f"{n:08b}")      # 01111011
print(f"{n:08o}")      # 00000173
print(f"{n:08x}")      # 0000007b
print(f"{n:08X}")      # 0000007B
n = 12.3456
print(f"{n:.2f}")      # 12.35
print(f"{n:8.2f}")     #    12.35
print(f"{n:.2e}")      # 1.23e+01
print(f"{n:.2E}")      # 1.23E+01
print(f"{n:.2g}")      # 1.23
print(f"{n:.2%}")      # 1234.56%
name = "Yamada"
age = 36
print(f"{name=}, {age=}")
byte_string = b"\xe3\x81\x82"
utf8_string = byte_string.decode()    # バイト列から文字列に変換
print(utf8_string)

utf8_string = "あ"
byte_string = utf8_string.encode()    # 文字列からバイト列に変換
print(byte_string)
utf8_str = "あ"
utf8_bytes = utf8_str.encode('utf-8')             # UTF-8バイト列: b'\xe3\x81\x82'
sjis_bytes = utf8_str.encode('sjis')              # Shift_JISバイト列: b'\x82\xa0'
cp932_bytes = utf8_str.encode('cp932')            # CP932バイト列: b'\x82\xa0'
eucjp_bytes = utf8_str.encode('euc_jp')           # EUC-JPバイト列: b'\xa4\xa2'
jis_bytes = utf8_str.encode('iso2022_jp')         # ISO-2022-JPバイト列: b'\x1b$B$"\x1b(B'

# UTF8/SJIS/CP932/EUC/JISバイト列からUnicode文字列への変換
utf8_str = utf8_bytes.decode('utf-8')             # あ
utf8_str = sjis_bytes.decode('sjis')              # あ
utf8_str = cp932_bytes.decode('cp932')            # あ
utf8_str = eucjp_bytes.decode('euc_jp')           # あ
utf8_str = jis_bytes.decode('iso2022_jp')
# coding: utf-8
print(len("あいうえお"))        # Python 2だと15、Python 3だと5
print(len(u"あいうえお"))
str = """A simple example module
This module is ...
"""
str = "Hello \
world!"
print("Hello " "world!")
print("%s" % "ABC")         #=> ABC
print("%d" % 123)           #=> 123
print("%f" % 1.23)          #=> 1.230000
print("%x" % 255)           #=> ff
print("%o" % 255)           #=> 377
print("%%%d" % 80)          #=> %80
print("|%5s|" % 'ABC')       #=> |  ABC| : 右寄せ5文字分
print("|%-5s|" % 'ABC')      #=> |ABC  | : 左寄せ5文字分
print("|%5d|" % 123)         #=> |  123| : 右寄せ5桁
print("|%-5d|" % 123)        #=> |123  | : 左寄せ5桁
print("|%+5d|" % 123)        #=> | +123| : ±符号付き
print("|%5.2f|" % 1.23)      #=> | 1.23| : 全体桁数.少数点以下の桁数
print("|%05d|" % 123)        #=> |00123| : 0埋め
