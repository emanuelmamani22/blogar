import random
from .models import Post



def generar_codigo():
    l=[['a','A','b','B','c','C'],['d','D','e','E','f','F'],['g','G','h','H','i','I'],['j','J','k','K','l','L'],['m','M','n','N','_','-'],['o','O','p','P','k','K'],['r','R','s','S','t','T'],['u','U','v','V','w','W'],['x','X','y','Y','z','Z'],['1','2','3','4','5','6']]
    a=random.randrange(10000000000,99999999999)
    b=str(a)
    s=''
    for x in b :
        n=0
        i=int(x)
        while True :
            if  i == n:
                r=random.randrange(0,5)
                s=s+l[i][r]
                break
            n=n+1
    if Post.objects.filter(codigo_e=s):
       generar_codigo()
    
    return s
