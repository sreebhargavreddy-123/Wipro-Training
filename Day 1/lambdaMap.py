add=lambda a,b: a+b
print(add(2,3))

# maxnum=lambda x,y: max(x,y)
maxnum=lambda x,y:x if x>y else y
print(maxnum(23,44))

numb=[1,2,3,4,5]
sq=list(map(lambda x:x*x,numb))
print(sq)