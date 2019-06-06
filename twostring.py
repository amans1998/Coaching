l1=[1,2,3,4]
l2=["a","b","c","d"]
l1.sort(reverse=True)
for m,n in zip(l1,l2):
    print(str(m)+n,end=",")
print()
for m,n in zip(l1,l2):
    print("[",m,",",n,"]")
