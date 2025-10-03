import math
numero=float(input("Ingrese un numero: "))
radio=float(input("Ingrese el radio de un circulo: "))
grados=float(input("Ingrese los grados a convertir: "))
#-------------procesos
#EJEMLO USO DE FUNCIONES
raiz=math.sqrt(numero)
seno=math.sin(numero)
coseno=math.cos(numero)
pi=math.pi
euler=math.e
potemncia=math.pow(numero,4)
factorial=math.factorial(10)
redondeoarriba=math.ceil(numero)
redondeoabajo=math.floor(numero)
logaritmo=math.log(numero)
#ejercicio
#AREA=PI*RARIO ELEVADO AL CUADRADO
#PERIMETRO=2*PI*RADIO
area=math.pi*(radio**2)#forma sin funciones
area2=math.pi*math.pow(radio,2)#forma con funciones math
perimetro=2*math.pi*radio
eulercubo=math.pow(math.e,3)
#convertir grados a radianes
radianes=math.radians(grados)
engrados=math.degrees(radianes)
#-----------------salidas
#print("La raiz cuadrada de",numero,"es:",raiz)#forma clasica
print(f"La raiz cuadrada de {numero} es: {raiz:.2f}")#forma moderna  
print(f"El seno de {numero} es: {seno:.2f}")
print(f"El coseno de {numero} es: {coseno:.2f}")  
print(f"El valor de pi es: {pi:.4f}") 
print(f"El valor de euler es: {euler:.4f}")
print(f"{numero} elevado a la 4 es: {potemncia:.2f}")
print(f"El factorial de 10 es: {factorial}")
print(f"El redondeo hacia arriba de {numero} es: {redondeoarriba}")
print(f"El redondeo hacia abajo de {numero} es: {redondeoabajo}")
print(f"El area del circulo de radio {radio} es: {area:.2f}")
print(f"El area del circulo de radio {radio} es: {area2:.2f}")
print(f"El perimetro del circulo de radio {radio} es: {perimetro:.2f}")
print(f"El valor de euler elevado a la 3 es: {eulercubo:.2f}")
print(f"El logaritmo natural de {numero} es: {logaritmo:.2f}")
print(f"{grados} grados en radianes es: {radianes:.2f}")
print(f"{radianes:.2f} radianes en grados es: {engrados:.2f}")

