import numpy as np
X=np.random.rand(5)
W=np.random.rand(5)
b=1
beta=1
v=0


def juncaoAditiva():
    u=0
    for i in range(len(X)):
        v=X[i]*W[i]
        u=u+v
        print(u)
    u=u-b
    print(u)
    return u

def main():
    z=juncaoAditiva()
    if (z>=0):
        y=1
        print(f"A rede neural foi ativada com valor a: {y}")
    elif (z<0):
        y=0
        print(f"A rede neural foi desativada com valor a: {y}")

if __name__ == "__main__":
    main()