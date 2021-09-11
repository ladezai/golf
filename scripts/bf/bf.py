import sys
T,P,S,N=None,0,[0]*30000,{">":"P+=1","<":"P-=1",".":"print(chr(S[P]),end='')",
",":"S[P]=ord(input())","+":"S[P]+=1","-":"S[P]-=1","[":"while S[P]:","]":"pass"}

def R(t):
    I=[]
    while len(t):
        c,*t=t;I.append(N[c]);
        if c=='[':q,t=R(t);I.append(q);
        if c==']':return (I,t);
    return I

def F(n,i=0):
    k=""
    for x in n:
        if type(x)==list:I=F(x,i+1);k+=I;
        else:k+="\t"*i+x+"\n";
    return k

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:*T,=filter(lambda x:x in N,"".join(f.readlines()));
    exec(F(R(T)))