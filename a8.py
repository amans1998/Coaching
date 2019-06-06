t=4,5,6
print(t)
print(t[1])
print(len(t))
print(t.count(4))
print(t.index(4))
print(max(t))
print(max(t))
print(sum(t))
print(tuple("Hello"))
print(tuple(range(2,10,2)))
def area():
    a=5
    b=7
    return a,b
c=area()
print(c)
l=[1,6,8,9]
d=tuple(l)
print(d)
e={}
e["name"]="Aman"
print(e)
print(e["name"])
n=[1,2,3]
li=["l","m"]
e["li"]=["Prakash",n]
print(e)
print(e.get("name"))
print(e.get("naddres"))
print(e.get("address","not found"))
d1=e.copy()
print(d1)
d2=dict.fromkeys(e)
print(d2)
print(e.setdefault("name","Rana"))
print(e.setdefault("address","Rana"))
