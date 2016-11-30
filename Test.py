import re

tuple=(("apple", "banana"),("grape", "orange"),("watermelon",),("grapefruit",))
for i in range(len(tuple)):
    print "tuple[%d]:"%i, "",
    for j in range(len(tuple[i])):
        print tuple[i][j], "",
    print

k=0
for a in map(None, tuple):
    print "tuple[%d];" % k, "",
    for x in a:
        print x, "",
    print
    k+=1


dict={"a":"apple", "b": "banana", "g": "grape", "o": "orange"}
print dict
print dict["a"]
print "%s, %(a)s, %(b)s" % {"a":"apple", "b": "banana"}
dict["w"]="watermelon"
print dict
del(dict["w"])
dict["g"]="grapefruit"
print dict
print dict.pop("b")
print dict
for k in dict:
    print "dict[%s];" % k,dict[k]

print dict.items()
for (k,v) in dict.items():
    print "dict[%s];" % k, v
print dict.iteritems()
print dict.iterkeys()
print dict.itervalues()
print dict.keys()
print dict.values()



def func(n):
    for i in range(n):
        yield i

for i in func(3):
    print i

r=func(3)
print r.next()
print r.next()
print r.next()


def reverse(s):
    return s[::-1]

def reverse1(s):
    li=list(s)
    li.reverse()
    s="".join(li)
    return s

print reverse("hello")
print reverse1("hello")

tel1="0791-1234567"
print re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel1)

tel2="010-12345678"
print re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel2)

tel3="(010)12345678"
#print re.findall(r"[\(]?\d{3}[\)-]?\d{8}", tel3)
print re.findall(r"[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}", tel3)

s="1abc23def45"
p=re.compile(r"\d+")
print p.findall(s)
print p.pattern

p=re.compile(r"(abc)\1")
m=p.match("abcabcabc")
print m.group(0)
print m.group(1)
print m.group()


context="hello world\n" \
        "hello china"
f=file("hello.txt", "w")
f.write(context)
f.close()

f=open("hello.txt")
while True:
    line=f.readline()
    if line:
        print line
    else:
        break
f.close()

f=open("hello.txt")
lines=f.readlines()
for line in lines:
    print line
f.close()


f=open("hello.txt")
context=f.read()
print context
f.close()







