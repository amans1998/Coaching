n="Hi this is Aman"
print(len(n))
print('h' in n)
print('hi' in n)
print(n.lower())
print(n.upper())
print(n)
print(n.isupper())
print(n.islower())
print(n.lower().islower())
print(n.upper().isupper())
print(n.istitle())
print(n.isalpha())
print(n.isalnum())
print(n.isspace())
f="12345"
print(n.isdigit())
print(n.isdigit())
print(n.startswith("h"))
print(n.startswith("H"))
print(n.endswith("Aman"))
print(n.endswith("aman"))
print(" Mr.".join(["aman","prakash"]))
print(",".join(["aman","prakash"]))
print(",".join(["aman","prakash","saurav"]))
m=n*3
print(m)
j="hi"+" "+"bye"
print(j)
ss=n.split()
print(ss)
sp=n.split("i")
print(sp)
print(n.rjust(40,"*"))
print(n.ljust(40,"*"))
print(n.center(40,"*"))
i="         hi its aman"
print(i.strip())
print(i.rstrip())
print(i.lstrip())
g="hhhhhhhhhhhhhhhTHIS IS AMANhhhhhhhhh"
print(g.strip("h"))
g="hhhhhhhhhhhhhhhfffffffffTHIS IS AMANffffffffhhhhhhhhh"
print(g.strip("h").strip("f"))
a,b,c,d,e="hello"
print(a)
print(b)
print(c)
print(d)
print(e)
print("hi ",end="its ")
print("aman")
print("a","b","c",sep="!")
for k in n:
    print(k,end="")
print()
for k in n:
    print(k)

