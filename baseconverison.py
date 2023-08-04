def convert(a,b,c):
    if a=='0':return 'a'
    t=0
    a=str(a)[::-1]
    for i in range(len(a)):
        t+=(len(b)**i)*b.index(a[i])
    r=''
    while t:
        r+=c[t%len(c)]
        t//=len(c)
    return r[::-1]
