#input 
par=0
impar=0

for i in range(100):
    n=int(input("digite un numero: "))
    c=n%2
    if c==0:
        par=par+1
    else:
        impar=impar+1
print("Cantidad de pares: "+str(par)+" Cantidad de impares: "+str(impar))
    
