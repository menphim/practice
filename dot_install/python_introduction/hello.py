# coding: UTF-8
# 変数(データにつけるラベル)

# データ型
# 数値
# 真偽値
# None
# 関数・オブジェクト
# 要素が並んだもの
# 文字列
# リスト
# タプル
# セット
# 辞書型
# 整数，小数，複素数

# 演算子 + - * / // % **

print 10*5
print 10 // 3.0
print 10/3
print 10 % 3
print 2**3

msg = "hello world"
print  msg#コメント

print  5+2.0

#整数同士の割り算 →　切り捨ての整数
print 10/3.0

# 文字列
# "Hello" 'hello'
# 日本後 u"こんにちは！"
# + *
print "hello " + "world"
print u"無駄" *10 +u"ァ！"
print 'hello \n wo\trld\\ it \'sapen'
print """<html lang = "ja">
<body>
</body>
</html>"""

# 文字数 len
# 検索 find
# 切り出し[]
s="abcdefghi"
print len(s)
print s.find("c")
print s.find("x")
#print len(s)
#print s.find("x")
print s[2]
print s[2:5]
print s[:5]
print s[2:]
print s[2:-1]

# 数値 <> 文字列

# 文字列 → 数値 int float
# 数値 → 文字列 str

print 5 + int ("5")
print 5 + float ("5")

age = 20
print "I am "+ str(age) + " years old!"

# リスト
sales = [255, 100,353, 400, 'aba']
# len + *

print len(sales)
print sales[2]
sales[2] = 100
print sales[2]

# in
print 100 in sales

# range
print range(3,10,2)

# sort / reverse

sales.sort()
print sales

sales.reverse()
print sales

# 文字列とリスト
d = "2013/12/15"
print d.split("/")

a= ["a","b","c"]
print "-".join(a)

# タプル(変更ができない)
a = (2,5,8)
#len + * []
print len(a)
print a*3

# a[2]=10

#タプル<>リスト
b = list(a)
print b

c = tuple(b)
print c

# セット(集合型) - 重複を許さない

a= set([1,2,3,4,3,2])
b= set([3,4,5])
print a
print b
print a-b

print a | b

print a & b

print a ^ b

# 辞書 key value
#[2505,523,500]
sales={"taguchi":200,"fkoji":300,"dotinstall":200}
print sales
print sales["taguchi"]
sales["fkoji"]=800
print sales
#in
print "taguchi" in sales # True

#keys, values, items
print sales.keys()
print sales.values()
print sales.items()


a=10
b=1.2345
c="taguchi"
d={"fkoji":200,"dotinstall":500}
print "age: %d" %a
print "age: %10d" %a
print "age: %010d" %a
print "price: %f" %b
print "price: %.2f" %b
print "name: %s" %c
print "sales: %(fkoji)d" %d
print "%d %f" %(a,b)

# 条件分岐 if
#比較演算子 > < >= <= == !=
# 論理演算子 and or not

score = 45
if score> 60:
#if score> 60 and score <80:
#if 60 < score < 80:
	print "ok!"
	print "ok!"
elif score>40:
	print "soso.."
else:
	print "ng!"

print "OK!" if score >50 else "NG!"

# for ループ
sales = [13,4523,31,238]
sum = 0
for sale in sales:
	sum += sale
	print sale
else:
	print sum
#countinue
for i in range(10):
	if i == 3:
		continue
	elif i==5:
		break
	print i

# for ループ
users = {"taguchi":200,"fkoji":300,"dotinstall":500}
for key, value in users.iteritems():
	print "key: %s value: %d"%(key,value)
for key, value in users.iteritems():
	print key
for key, value in users.iteritems():
	print value

# while ループ
n = 0
while n<10:
	if n==3:
		n+=1
		continue
	elif n==8:
		break
	print n
	n+=1
else : print "end"

# 関数
# 引数
def hello(name,num=3):
	print "hello %s!" % name * num
	return"hello %s!" % name * num


hello("tom",2)
hello("steve",3)
hello("steve")
hello(num=5,name="tom")
s=hello(num=5,name="tom")
print s*3


# 変数のスコープ
name = "taguchi"
def hello():
	name = "fkoji"
print name

# pass
def hello2():
	pass

# リスト <> 関数 map
# 無名関数
def double(x):
	return x *x
print map(double,[2,5,8])
print map(lambda x:x*x,[2,5,8])

# オブジェクト(変数と関数をまとめたもの)
# クラス：オブジェクトの設計図
# インスタンス：クラスを実体化したもの

class User(object):
	def __init__(self, name):
		self.name =name
	def greet(self):
		print "my name is %s!" % self.name

bob = User("Bob")
tom = User("Tom")

print bob.name
print tom.name
bob.greet()

class SuperUser(User):
	def shout(self):
		print "%s is SUPER!!" % self.name

tony = SuperUser("Tome")
tony.greet()
tony.shout()

# モジュール
import math,random
from datetime import date as d
print math.ceil(5.2)
for i in range(5):
	print random.random()
print d.today()