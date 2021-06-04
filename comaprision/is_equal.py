""" 
diff betwwen the is and ==


"""
#effect on immutable datatype
print('effect on immutable datatype')
a = 1
b = 1
c = a
print(a == b)

print(a is b)

print(id(a))
print(id(b))
print(id(c))
c = 10
print(a,c)
#effect on mutable datatype
print('effect on mutable datatype')
a = {'a' : 1}
b = {'a' : 1}
print(a == b)

print(a is b) #beacuse their id are different

print(id(a))
print(id(b))