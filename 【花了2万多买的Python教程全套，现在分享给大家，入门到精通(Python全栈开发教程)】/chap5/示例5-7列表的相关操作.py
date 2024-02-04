lst=['hello','world','python']
print('原列表',lst,id(lst))
lst.append('c++')
print('添加元素后',lst,id(lst))
lst.insert(2,'java')
print('插入元素后',lst,id(lst))
lst.remove('world')
print('删除元素后',lst,id(lst))
lst.pop()
print('删除末尾元素后',lst,id(lst))
lst.clear()
print('清空列表后',lst,id(lst))

#
lst=['hello','world','python']
print('原列表',lst,id(lst))
lst.reverse()
print('翻转列表后',lst,id(lst))
new_lst=lst.copy()
print('复制列表后',new_lst,id(new_lst))

lst[1]='html'
print('修改元素后',lst,id(lst))