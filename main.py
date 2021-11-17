def merge(*lists):
    n = len(lists)
    m = 0
    ans = []
    mn=-1
    
    for i in range(n):
        m+=len(lists[i])
    
    f = False
    
    while(m>0):
        if f:
            f=False
            for i in range(n):
               if len(lists[i])>0 and lists[i][0]==mn:
                   f=True
                   m-=1
                   ans.append(lists[i].pop(0))
        else:
            f=True
            mn=-1
            for i in range(n):
                if len(lists[i])>0:
                    if mn==-1:
                        mn=lists[i][0]
                    else:
                        mn=min(mn,lists[i][0])
    return ans
