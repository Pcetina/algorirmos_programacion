a=0

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))


while(dividendo>=divisor):
    a=a+1;
    dividendo=dividendo-divisor;

print("Cociente: ",a)
print("Modulo: ",dividendo )



