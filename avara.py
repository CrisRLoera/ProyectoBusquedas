class State:
    father: any
    def __init__(self, name, chils, f):
        self.name=name
        self.chils=chils
        self.f=f

        
dlr =[[0,1.8,2.5,2.8,4.5,5.0,3.0,5.5,5.8,6.4],
      [1.8,0,4.4,5.6,3.5,2.3,4.5,3.2,8.6,10.8],
      [2.5,4.4,0,3.8,3.4,8.0,6.3,7.7,4.0,9.5],
      [2.8,5.6,3.8,0,7.7,8.0,2.8,10.0,3.0,4.6],
      [4.5,3.5,3.4,7.7,0,6.7,6.8,4.0,8.7,13.5],
      [5.0,2.3,8.0,8.0,6.7,0,5.3,3.5,11.8,12.3],
      [3.0,4.5,6.3,2.8,6.8,5.3,0,6.6,7.5,6.8],
      [5.5,3.2,7.7,10.0,4.0,3.5,6.6,0,12.5,15.2],
      [5.8,8.6,4.0,3.0,8.7,11.8,7.5,12.5,0,6.4],
      [6.4,10.8,9.5,4.6,13.5,12.3,6.8,15.2,6.4,0]]


def initValues():
    for i in range(0,len(ListStates)):
        if EndS[0].name == ListStates[i].name:
            for j in range(0,10):
                ListStates[j].f=dlr[i][j]



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
        if CurrentS[0].name == EndS[0].name:
            meta = True
            return True
    
        ExOpen()
        

        CurrentS[0]=Siguiente()

        AddClose()
        num+=1

        if num >=trys:
            meta=True
            return False

def Siguiente():
    best=OpenL[0]
    for i in OpenL:
        if (i.f<=best.f):
            best=i
    return best
    

def ExOpen():
    iterr=0
    for i in CurrentS[0].chils:
        iterr+=1
        if existIn(i,OpenL) == False:
            pass
        else:
            OpenL.append(i)
    for i in OpenL:
        i.father=CurrentS[0].name
    
def AddClose():
    if len(CloseL)!=0:
        if(existIn(CurrentS[0],CloseL)):
            CloseL.append(CurrentS[0])

    else:
        CloseL.append(CurrentS[0])
        

def existIn(obj,lista):
    iterr=0
    if len(lista) != 0:
        for i in range(0,len(lista)):
            iterr+=1
            if obj.name == lista[i].name:
                return False
            else:
                pass

    else:
        return True
    return True

def selection(wordSerch):
    for i in ListStates:
        if i.name == wordSerch:
            return i


ListStates=[A,B,C,D,E,F,G,H,I,J]
CurrentS = []
EndS = []
print("Ingrese el estado inicial en mayusculas: ")
CurrentS.append(selection(input()))
print("Ingrese el estado final en mayusculas: ")
EndS.append(selection(input()))
print("Ingrese el limite de intentos: ")
trys=int(input())
OpenL = []
CloseL = [A]
CloseL[0]=CurrentS[0]

initValues()

findS=BusquedaAvara()

if findS == True:
    print("La respuesta es: ")
    for i in CloseL:
        print(i.name)
else:
    print("No se encontro respuesta")

