class State:
    father: any
    def __init__(self, name, chils, f):
        self.name=name
        self.chils=chils
        self.f=f

#Implementacion de estados personalizados

#print("Ingrese el valor heuristico para A")
#numA=int(input())
#print("Ingrese el valor heuristico para B")
#numB=int(input())
#print("Ingrese el valor heuristico para C")
#numC=int(input())
#print("Ingrese el valor heuristico para D")
#numD=int(input())
#print("Ingrese el valor heuristico para E")
#numE=int(input())
#print("Ingrese el valor heuristico para F")
#numF=int(input())
#print("Ingrese el valor heuristico para G")
#numG=int(input())
#print("Ingrese el valor heuristico para H")
#numH=int(input())
#print("Ingrese el valor heuristico para I")
#numI=int(input())
#print("Ingrese el valor heuristico para J"#)
#numJ=int(input())

#Nodos por defecto

A = State('A',[],12)
B = State('B',[],7)
C = State('C',[],10)
D = State('D',[],15)
E = State('E',[],6)
F = State('F',[],5)
G = State('G',[],11)
H = State('H',[],0)
I = State('I',[],13)
J = State('J',[],20)

A.chils=[E,G]
B.chils=[H,F]
C.chils=[E,D,I]
D.chils=[C,J]
E.chils=[A,C,H]
F.chils=[B,H,G]
G.chils=[F,A,J]
H.chils=[E,B,F]
I.chils=[C,J]
J.chils=[I,D,G]

def BusquedaAvara():
    meta=False
    num=0
    while(meta == False):
        #print("Estado actual",CurrentS[0].name)
        if CurrentS[0].name == EndS[0].name:
            #print("Se llego a la meta")
            meta = True
            return True
    
        #print("En Abiertos")
        for i in OpenL:
            break
            #print(i.name)
        #print("En Cerrados")
        #print(len(CloseL))
        for i in range(0,len(CloseL)):
            break
            #print(CloseL[i])
            #print(CloseL[i].name)
        #print("Expandiendo Abiertos")
        ExOpen()
        #print("En Abiertos tras expandir")
        for i in OpenL:
            break
            #print(i.name," ",i.f)
        

        CurrentS[0]=Siguiente()

        #print("Agregando a Cerrados")
        AddClose()
        num+=1
        #print("Fin de ciclo:", num)

        if num >=trys:
            meta=True
            return False

def Siguiente():
    best=OpenL[0]
    for i in OpenL:
        if (i.f<=best.f):
            best=i
    #print("El mejor es:",best.name)
    return best
    

def ExOpen():
    iterr=0
    #print("---Dentro de funcion exOpen---")
    for i in CurrentS[0].chils:
        iterr+=1
        #print(" Iteracion:",iterr )
        #print("Existe en Abiertos:",existIn(i,OpenL))
        if existIn(i,OpenL) == False:
            pass
            #print("No se agrego ", i.name)
        else:
            OpenL.append(i)
            #print("Se agrego:",i.name)
    for i in OpenL:
        i.father=CurrentS[0].name
        #print(i.father, "padre de", i.name)
    
def AddClose():
    #print("---Dentro de funcion addClose---")
    #print("Existe?")
    #print(existIn(CurrentS[0],CloseL))
    if len(CloseL)!=0:
        if(existIn(CurrentS[0],CloseL)):
            CloseL.append(CurrentS[0])

        for i in range(0,len(CloseL)):
            break
            #print(CloseL[i].name)
    else:
        CloseL.append(CurrentS[0])
        

def existIn(obj,lista):
    #print("---Dentro de funcion exist--")
    #print(len(lista))
    iterr=0
    if len(lista) != 0:
        for i in range(0,len(lista)):
            iterr+=1
            #print("Iteraccion existIn:", iterr)
            #print(obj.name,"==",lista[i].name)
            #print(lista[i].name)
            if obj.name == lista[i].name:
                #print("Existe")
                return False
            else:
                pass
                #print("No existe")

    else:
        #print("lista vacia")
        return True
    #print("Fin de ejecucion")
    return True
def selection(wordSerch):
    for i in ListStates:
        if i.name == wordSerch:
            return i


ListStates=[A,B,C,D,E,F,G,H,I,J]
CurrentS = []
EndS = []
print("Ingrese el nodo inicial en mayusculas: ")
CurrentS.append(selection(input()))
print("Ingrese el nodo inicial en mayusculas: ")
EndS.append(selection(input()))
print("Ingrese el limite de intentos: ")
trys=int(input())
OpenL = []
CloseL = [A]
CloseL[0]=CurrentS[0]
print(CloseL[0].name)
findS=BusquedaAvara()

if findS == True:
    print("La respuesta es: ")
    for i in CloseL:
        print(i.name)
else:
    print("No se encontro respuesta")

