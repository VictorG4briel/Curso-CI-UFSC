#aula 09/09
#função
##a=int(input("Digite o valor de a:"))
##b=int(input("Digite o valor de b:"))
##c=0

##def soma():
    #c= a + b
    #print(c)
    #return c

##def main():
    #c=soma()
    #d=c+1
    #print(d)

#if __name__ == "__main__":
    #main()

#função
import numpy as np
X=np.random.rand(5)
W=np.random.rand(5)
b=1
v=0


def juncaoAditiva():
    u=0
    print(X)
    print(W)
    for i in range(len(X)):
        v=X[i]*W[i]
        u=u+v
        print(v)
        print(u)
    u=u-b
    print(u)
    return u

def main():
    z=juncaoAditiva()
    print(z)
    if (z>=0):
        y=1
        print(f"A rede neural foi ativada com valor a: {y}")
    elif (z<0):
        y=0
        print(f"A rede neural foi desativada com valor a: {y}")

if __name__ == "__main__":
    main()