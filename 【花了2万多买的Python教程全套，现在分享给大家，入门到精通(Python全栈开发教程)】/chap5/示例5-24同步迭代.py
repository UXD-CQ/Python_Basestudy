fruits=['apple','banana','apple','orange']
counts=[12,6,7,10,12,6]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',12:
            print('苹果，12个')
        case 'banana',6:
            print('香蕉，6个')
        case 'orange',10:
            print('橙子，10个')