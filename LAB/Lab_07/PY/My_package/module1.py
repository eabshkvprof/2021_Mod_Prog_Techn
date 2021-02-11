def func1(x):
    k=0 # лічильник
    imax=0 # номер максимального елементу
    max=x[0] # значення максимального елементу
    # сортування масиву
    while k<len(x)-1: 
        j=k
        imax=k
        max=x[k]
        while j<len(x):
            if max<x[j]:
                max=x[j]
                imax=j
            j+=1
        x[imax]=x[k]
        x[k]=max   
        k+=1
    y=[] # створення нового масиву
    # перенесення неповторюваних елементів до нового масиву
    for i in range(len(x)):
        buf=x[i]
        num=0
        for j in range(len(x)):
            if x[i]==x[j]:
                num+=1
        if num==1:
            y=y+[x[i]]
    return y