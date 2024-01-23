t=(i for i in range(1,4))
print(t)
# t=tuple(t)
# print(t)

print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)