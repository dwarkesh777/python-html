def ramanujan(limit):
    result=""
    for a in range(1,limit):
        for b in range (a,limit):
            for c in range(a,limit):
                for d in range(c,limit):
                    x=a**3+b**3
                    y=c**3+d**3
                    if x==y and (a!=c or b!=d):
                        number = a**3+b**3
                        result+=f'{number}:{a,b,c,d}'
    return result
print (ramanujan(20))
