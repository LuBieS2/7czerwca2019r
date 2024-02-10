def rozsztfruj(S, k):
    n=len(S)
    T=[]
    w=n//k
    m=1
    temp=[]
    Si=[]
    for i in range(len(S)):
        temp.append(S[i])
        if i==(w*m)-1:
            Si.append(temp)
            m+=1
            temp=[]
    for n in range(w):
        if n%2==0:
            for i in range(len(Si)):
                T.append(Si[i][n])
        else:
            for i in range(len(Si)):
                T.append(Si[abs(len(Si)-1-i)][n])
S="NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"
S=list(S)
rozsztfruj(S, 10)