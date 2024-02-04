lst=[99,33,55,97,32,54,88,96,75,87,12,98,3]
print('原列表',lst)
asc_lst=sorted(lst)
print('升序排序',asc_lst)
print('原列表',lst)

desc_lst=sorted(lst,reverse=True)
print('降序排序',desc_lst)
print('原列表',lst)

lst2=['a','z','f','D','banner','Orange','C']
print('原列表',lst2)
new_lst2=sorted(lst2,key=str.lower)
print('升序排序',new_lst2)
print('原列表',lst2)
