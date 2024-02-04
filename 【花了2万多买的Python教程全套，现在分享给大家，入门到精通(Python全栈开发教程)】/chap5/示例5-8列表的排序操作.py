lst=[99,33,55,97,32,54,88,96,75,87,12,98,3]
print('原列表',lst)
lst.sort()
print('升序后',lst)

lst.sort(reverse=True)
print('降序后',lst)

lst2=['a','z','f','D','x','h','C']
print('原列表',lst2)
lst2.sort()
print('升序后',lst2)

lst2.sort(reverse=True)
print('降序后',lst2)

lst2.sort(key=str.lower)
print('忽略大小写排序后',lst2)