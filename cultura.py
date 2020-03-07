#Jhonmaiker Zerpa
#Dayerleen Gonzalez
#Marifel
#Angel Romero
#cindy
#Danyelis Marcano


class juego():

    def VerificarDos(self,cadena, numero , lista =[]):
        if cadena == lista[numero]:
            return True;
        else :
            return False

    
    def Repetido(self, cadena , lista = []):
        return cadena in lista
        
    


elemento=""
salio=False
categoria = ""
jugadores = 0

cultura = juego()

listaObjetos = []

print("|||   BIENVENIDO A CULTURA CHUPISTICA |||")
print("")

while True :
    try:
        jugadores = int(input("Numero de jugadores en la partida : "))
        print("")
        break
    except:
        print("Solo se aceptan numeros...")
        print("")


categoria = input ("Ingrese la categoria: ")

print("")
print("Cultura chupistica de " + categoria)
print("")

while jugadores != 1 :
    contador=0
    print("")
    if listaObjetos :
        print("Repita los elementos anteriores...")
        print("")
        for i in range(len(listaObjetos)):
            elemento = input("elemento : ")
            if cultura.VerificarDos(elemento,contador,listaObjetos) == True :
                print("bien!!")
                print("")
                salio=False
                contador = contador + 1
            else :
                print ("Has fallado en el orden!!")
                salio=True
                break
        if salio == True :
            print("Has perdido el juego")
            print("la respuesta correcta era: ", listaObjetos)
            print("")
            print("")
            print("siguiente jugador...")
            jugadores  = jugadores - 1
        else:
            elemento = input ("Ahora ingrese su nuevo elemento: ")
            if cultura.Repetido(elemento,listaObjetos)==True:
                print("Este elemento ya  fue dicho!!")
                print("Has perdido!!")
                print("Los elementos hasta ahora eran:" , listaObjetos)
                print("")
                print("")
                print("Siguiente jugador...")
                jugadores = jugadores - 1 
            else:
                listaObjetos.append(elemento)
                print("Elemento añadido!!")
                print("")
                print("")
                print("siguiente jugador")
    else:
        elemento = input("Ingrese un elemento: ")
        print("elemento añadido")
        print("")
        print("")
        print("Siguiente jugador...")
        listaObjetos.append(elemento)


print("Ya solo queda un jugador")
print ("Felicidades!!")
print("|||   HAS GANADO   |||")
  
            
                   
        


    
