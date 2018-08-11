def mostrar(lista, a, b, x):
    try:
        while lista[a] == x:
            a-=1
            if(a<0):
                raise IndexError
        print(lista[a], end=" ")
    except IndexError:
        print("X", end=" ")
    try:
        while lista[b] == x:
            b+=1
            if(b<0):
                raise IndexError
        print(lista[b])        
    except IndexError:
        print("X")

def buscaAltura(x, MIN, MAX, lista):
    
    if(MIN > MAX):
        #print(str(MAX)+" "+str(MIN))
        mostrar(lista, MAX, MIN, x)
        return

    mid = (MAX+MIN) // 2

    if(lista[mid] == x):
        #print(str(mid-1)+" "+str(mid+1))
        mostrar(lista, mid-1, mid+1, x)
    elif(lista[mid] > x):
        buscaAltura(x, MIN, mid-1, lista)
    else:
        buscaAltura(x, mid+1, MAX, lista)

    

N = int(input())

alturas = [int(x) for x in input().split()]

Q = int(input())

busca = [int(x) for x in input().split()]

for x in busca:
    #print(x)
    buscaAltura(x, 0, N-1, alturas)
    #print("")
