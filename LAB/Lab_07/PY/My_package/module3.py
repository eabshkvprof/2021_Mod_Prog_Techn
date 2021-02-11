def func3(x):
    k=0 # лічильник
    imin=0 # номер мінімального елементу
    min=x[0] # значення мінімального елементу
    while k<len(x)-1: 
        j=k
        imin=k
        min=x[k]
        while j<len(x):
            if min>x[j]:
                min=x[j]
                imin=j
            j+=1
        x[imin]=x[k]
        x[k]=min   
        k+=1
    return x