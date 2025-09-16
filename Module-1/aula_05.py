#aula 10/09
#funções

#importação

import numpy as np
X=np.random.rand(5)
W=np.random.rand(5)
b=1
beta=0.25
v=0


def juncaoAditiva():
    u=0
    for i in range(len(X)):
        M=W[i] 
        if (W[i]<0.5):
            M=W[i] + 0.5
            print(M)
        N=X[i]
        if (X[i]<0.5):
            N=X[i] + 0.5
        print(N)
        v=N[i]*M[i]
        u=u+v
        print(u)
    u=u-b
    return u

def main():
    z=juncaoAditiva()
    a=1*beta*z
    y=1/(1+np.exp(a))
    print(f"A saida do meu neuronio é {y}")

if __name__ == "__main__":
    main()